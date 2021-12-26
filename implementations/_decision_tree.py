from __future__ import annotations

import numpy as np
import pandas as pd
from enum import Enum
from typing import Any, Tuple
from dataclasses import dataclass


class DecisionTree:

    class Criterion(Enum):
        GINI = "gini"
        ENTROPY = "entropy"

    @dataclass
    class Decision:
        left: bool
        right: bool

    @dataclass
    class Node:
        feature: str
        index: int
        value: Any
        purity: float
        depth: int
        is_terminal: bool = False
        left: DecisionTree.Node = None
        right: DecisionTree.Node = None
        decision: DecisionTree.Decision = None

    @dataclass
    class Split:
        purity: float
        feature: str
        index: int
        left_size: int
        right_size: int
        decision: DecisionTree.Decision = None

    def __init__(self, criterion: Criterion, max_depth: int, min_node_size: int):
        self.criterion = criterion
        self.root_node = None
        self.max_depth = max_depth
        self.min_node_size = min_node_size
        self.node_count = 0

    @staticmethod
    def _partition_by_feature(dataset: pd.DataFrame, labels: str, feature: str, index: int) -> np.ndarray:
        """
        Create a matrix with two columns, the first with the code (0 or 1) of the leaf node and the second
        with the corresponding class after partition the dataset by the specified feature.
        """
        value = dataset[feature].iloc[index]
        partition = dataset[[feature, labels]].copy()
        partition["Groups"] = partition[feature] < value
        partition["Classes"] = dataset[labels]
        return partition[["Groups", "Classes"]].to_numpy()

    def _measure_purity(self, data: np.ndarray) -> Tuple[float, int, int, int, int]:
        def _compute_entropy(node_data: np.ndarray) -> float:
            if len(node_data):
                y = node_data[:, 1]
                p1 = len(node_data[y == 1]) / len(node_data)
                p1logp1 = 0 if p1 == 0 else p1*np.log2(p1)
                p2 = len(node_data[y == 0]) / len(node_data)
                p2logp2 = 0 if p2 == 0 else p2*np.log2(p2)
                return - (p1logp1 + p2logp2)
            else:
                return 0

        def _compute_gini(node_data) -> float:
            if len(node_data):
                y = node_data[:, 1]
                return 1 - ((len(node_data[y == 1]) / len(node_data))**2 + (len(node_data[y == 0]) / len(node_data))**2)
            else:
                return 0

        def decision_for_leaf(node_data: np.ndarray) -> int:
            y = node_data[:, 1]
            return 1 if len(node_data[y == 1]) > len(node_data[y == 0]) else 0

        group_1 = data[data[:, 0] == 1]
        group_2 = data[data[:, 0] == 0]
        purity1 = _compute_gini(group_1) if self.criterion == DecisionTree.Criterion.GINI else _compute_entropy(group_1)
        purity2 = _compute_gini(group_2) if self.criterion == DecisionTree.Criterion.GINI else _compute_entropy(group_2)

        ldecision = decision_for_leaf(group_1)
        rdecision = decision_for_leaf(group_2)

        len_group1 = len(group_1)
        len_group2 = len(group_2)
        weighted_purity = purity1 * len_group1 / len(data) + purity2 * len_group2 / len(data)

        return weighted_purity, len_group1, len_group2, ldecision, rdecision

    def _find_split_point(self, records: pd.DataFrame, labels: str) -> Split:
        best_purity = float("inf")
        for feature in records.columns.drop(labels):
            for index in range(len(records)):
                partition = DecisionTree._partition_by_feature(records, labels, feature, index)
                purity, len_left, len_right, left_decision, right_decision = self._measure_purity(partition)
                if purity < best_purity:
                    best_feature = feature
                    best_index = index
                    best_purity = purity
                    best_left_size = len_left
                    best_right_size = len_right
                    best_left_decision = left_decision
                    best_right_decision = right_decision

        return DecisionTree.Split(
            purity=best_purity,
            feature=best_feature,
            index=best_index,
            left_size=best_left_size,
            right_size=best_right_size,
            decision=DecisionTree.Decision(left=best_left_decision, right=best_right_decision)
        )

    def _create_node(self, dataset: pd.DataFrame, labels: str, parent_depth: int) -> Tuple[Node, bool]:
        split = self._find_split_point(dataset, labels)

        self.node_count = self.node_count + 1
        print(f"Total number of nodes increased to: {self.node_count}")

        # Criteria to determine if the node is terminal
        has_small_child = (
            True if split.left_size < self.min_node_size or split.right_size < self.min_node_size else False
        )
        is_too_deep = True if parent_depth + 1 == self.max_depth else False
        is_parent_terminal = has_small_child or is_too_deep

        return DecisionTree.Node(
            feature=split.feature,
            index=split.index,
            value=dataset[split.feature].iloc[split.index],
            purity=split.purity,
            depth=parent_depth + 1,
            decision=split.decision
        ), is_parent_terminal

    def _get_node_data(self, dataset: pd.DataFrame, labels: str, node: Node):
        left_df = dataset[dataset[node.feature] < node.value]
        right_df = dataset[dataset[node.feature] >= node.value]

        left_node, is_node_terminal_l = self._create_node(left_df, labels, node.depth)
        right_node, is_node_terminal_r = self._create_node(right_df, labels, node.depth)

        if is_node_terminal_l or is_node_terminal_r:
            node.is_terminal = True
        else:
            node.left = left_node
            node.right = right_node
            node.left.depth = node.depth + 1
            node.right.depth = node.depth + 1
            print(f"new split node: {node.left} created with {len(left_df)} records.")
            print(f"new split node: {node.right} created with {len(right_df)} records.")

            self._get_node_data(left_df, labels, node.left)
            self._get_node_data(right_df, labels, node.right)

    def train(self, dataset: pd.DataFrame, labels: str) -> None:
        self.root_node, is_root_terminal = self._create_node(dataset, labels, parent_depth=0)

        if is_root_terminal:
            print("Warning: Root node is terminal.")
        else:
            self._get_node_data(dataset, labels, self.root_node)

        print("train finished.")

    def predict(self, x: pd.DataFrame) -> np.ndarray:
        def predict_row(row: pd.Series) -> int:
            # Find terminal node
            node: DecisionTree.Node = self.root_node
            while not node.is_terminal:
                node = node.left if row[node.feature] < node.value else node.right

            return node.decision.left if row[node.feature] < node.value else node.decision.right

        return x.apply(predict_row, axis=1).to_numpy()
