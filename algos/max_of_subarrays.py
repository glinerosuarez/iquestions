"""
Given an array and an integer A, find the maximum for each contiguous subarray of size A.

Input: array = [1, 2, 3, 1, 4, 5, 2, 3, 6], A = 3
Output: 3 3 4 5 5 5 6

Below is a more detailed walkthrough of what you should be trying to code, using the example above:
subarray 1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
maximum of subarray 1 = 3
subarray 2 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
maximum of subarray 2 = 3
subarray 3 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
maximum of subarray 3 = 4
Etc.
"""
from __future__ import annotations

from collections import deque
from typing import List, Optional
from dataclasses import dataclass


def solution(a: List[int], k: int) -> List[int]:
    def max(a):
        _max = float("-inf")
        for e in a:
            if e > _max:
                _max = e
        return _max

    res = list()

    for i in range(len(a) - k + 1):
        res.append(max(a[i:i+k]))

    return res


@dataclass
class Node:
    val: int
    left: Optional[Node] = None
    right: Optional[Node] = None
    height: int = 1


class AVLTree:

    @staticmethod
    def get_height(node: Optional[Node]) -> int: return node.height if node else 0

    @staticmethod
    def get_balance(parent: Optional[Node]) -> int:
        return AVLTree.get_height(parent.left) - AVLTree.get_height(parent.right) if parent else 0

    @staticmethod
    def right_rotate(z: Node):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        # Return the new new parent
        return y

    @staticmethod
    def left_rotate(z: Node):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        # Return the new new parent
        return y

    def insert(self, parent: Node, value: int):
        # Step 1: perform normal BST insertion.
        if parent:
            if value < parent.val:
                parent.left = self.insert(parent.left, value)
            else:
                parent.right = self.insert(parent.right, value)
        else:
            return Node(value)
        # Step 2: Update the height of the parent node.
        parent.height = 1 + max(AVLTree.get_height(parent.left), AVLTree.get_height(parent.right))
        # Step 3: Get balance factor
        balance = AVLTree.get_balance(parent)
        # Step 4: If the node is unbalanced, then try out the 4 cases
        # Case 1: left left
        if balance > 1 and value < parent.left.val: return AVLTree.right_rotate(parent)
        # Case 2: right right
        if balance < -1 and value > parent.right.val: return AVLTree.left_rotate(parent)
        # Case 3: left right
        if balance > 1 and value > parent.left.val:
            parent.left = AVLTree.left_rotate(parent.left)
            return AVLTree.right_rotate(parent)
        # Case 4 right left
        if balance < -1 and value < parent.right.val:
            parent.right = AVLTree.right_rotate(parent.right)
            return AVLTree.left_rotate(parent)
        return parent

    def delete(self, parent: Node, value: int) -> Optional[Node]:
        # Step 1: perform standard BST delete
        if not parent: return parent
        elif value < parent.val: parent.left = self.delete(parent.left, value)
        elif value > parent.val: parent.right = self.delete(parent.right, value)
        else:
            if parent.left is None:
                temp = parent.right
                parent = None
                return temp
            elif parent.right is None:
                temp = parent.left
                parent = None
                return temp
            temp = self.get_min_value_node(parent.right)
            parent.val = temp.val
            parent.right = self.delete(parent.right, temp.val)

        # If the tree has only one node,
        # simply return it
        if parent is None:
            return parent

        # Step 2 - Update the height of the
        # ancestor node
        parent.height = 1 + max(self.get_height(parent.left),
                              self.get_height(parent.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(parent)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - left left
        if balance > 1 and self.get_balance(parent.left) >= 0:
            return self.right_rotate(parent)

        # Case 2 - Right Right
        if balance < -1 and self.get_balance(parent.right) <= 0:
            return self.left_rotate(parent)

        # Case 3 - Left Right
        if balance > 1 and self.get_balance(parent.left) < 0:
            parent.left = self.left_rotate(parent.left)
            return self.right_rotate(parent)

        # Case 4 - Right Left
        if balance < -1 and self.get_balance(parent.right) > 0:
            parent.right = self.right_rotate(parent.right)
            return self.left_rotate(parent)

        return parent

    def get_min_value_node(self, parent: Optional[Node]) -> Optional[Node]:
        return parent if any([parent is None, parent.left is None]) else self.get_min_value_node(parent.left)

    def get_max_value_node(self, parent: Optional[Node]) -> Optional[Node]:
        return parent if any([parent is None, parent.right is None]) else self.get_max_value_node(parent.right)


def avl_solution(a: List[int], k: int) -> List[int]:
    tree = AVLTree()
    parent = None
    result = []

    # initial tree
    for e in a[:k]:
        parent = tree.insert(parent, e)
    result.append(tree.get_max_value_node(parent).val)
    parent = tree.delete(parent, a[0])

    for i in range(k, len(a)):
        parent = tree.insert(parent, a[i])
        result.append(tree.get_max_value_node(parent).val)
        parent = tree.delete(parent, a[i - k])

    return result


def deque_solution(a: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    for i in range(k):
        while q and a[i] >= a[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, len(a)):
        res.append(a[q[0]])
        while q and q[0] <= i-k:
            # remove from front of deque
            q.popleft()

        # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while q and a[i] >= a[q[-1]]:
            q.pop()

        # Add current element at the rear of Qi
        q.append(i)

    res.append(a[q[0]])
    return res


if __name__ == '__main__':

    print(deque_solution([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
