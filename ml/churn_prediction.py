"""
Given the following
[dataset](https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/teleco_user_data.csv),
can you create a decision tree to predict customer churn? For simplicity, you can set the maximum depth of the decision
tree to 4. For the purpose of this exercise, you do not need to optimize the model.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Any, Tuple
from dataclasses import dataclass
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


df = pd.read_csv(
    "https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/teleco_user_data.csv"
)
df['Churn'] = df.Churn.apply(lambda x: 1 if x == 'Yes' else 0)


class DecisionTree:
    @dataclass
    class Decision:
        left: bool
        right: bool

    @dataclass
    class Node:
        feature: str
        index: int
        value: Any
        gini: float
        depth: int
        is_terminal: bool = False
        left: DecisionTree.Node = None
        right: DecisionTree.Node = None
        decision: DecisionTree.Decision = None

    @dataclass
    class Split:
        gini: float
        feature: str
        index: int
        left_size: int
        right_size: int
        decision: DecisionTree.Decision = None

    def __init__(self, max_depth: int, min_node_size: int):
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

    @staticmethod
    def _gini_index(data: np.ndarray) -> Tuple[float, int, int, int, int]:
        def gini_for_leaf(node_data):
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
        gini_1 = gini_for_leaf(group_1)
        gini_2 = gini_for_leaf(group_2)

        ldecision = decision_for_leaf(group_1)
        rdecision = decision_for_leaf(group_2)

        len_group1 = len(group_1)
        len_group2 = len(group_2)
        weighted_gini = gini_1 * len_group1 / len(data) + gini_2 * len_group2 / len(data)

        return weighted_gini, len_group1, len_group2, ldecision, rdecision

    @staticmethod
    def _find_split_point(records: pd.DataFrame, labels: str) -> Split:
        best_gini = float("inf")
        for feature in records.columns.drop(labels):
            for index in range(len(records)):
                partition = DecisionTree._partition_by_feature(records, labels, feature, index)
                gini, len_left, len_right, left_decision, right_decision = DecisionTree._gini_index(partition)
                if gini < best_gini:
                    # print("New best split found")
                    # print(f"Feature: {feature} Value: {dataset[feature].iloc[index]} Index: {index} Gini score: {gini:0.5}")
                    best_feature = feature
                    best_index = index
                    best_gini = gini
                    best_left_size = len_left
                    best_right_size = len_right
                    best_left_decision = left_decision
                    best_right_decision = right_decision

        return DecisionTree.Split(
            gini=best_gini,
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
            gini=split.gini,
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


if __name__ == '__main__':
    # Read dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/erood/interviewqs.com_code_snippets/master/Datasets/teleco_user_data.csv"
    )
    df['Churn'] = df.Churn.apply(lambda x: 1 if x == 'Yes' else 0)  # Cast labels to int

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        df.iloc[:, :-1],
        df.iloc[:, -1:],
        test_size=0.20,
        random_state=42
    )
    model = DecisionTree(max_depth=3, min_node_size=0)
    model.train(pd.concat([X_train, y_train], axis=1), "Churn")

    # Compute accuracy
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):0.2%}")
