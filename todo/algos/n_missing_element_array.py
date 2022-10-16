"""
Suppose you're given an unsorted array, a. The array is intended to have all integer elements between its minimum and maximum, but could be missing some elements. Write a python function to find the n-th missing element in the array.

Consider the array in sorted order, then find the n-th missing number. If the n-th missing number does not exist, you can output 'Does not exist'.

Examples:


Input: a = [2, 3, 11, 9], n = 3


Output: 6


Missing elements in array: [4, 5, 6, 7, 8, 10]. So, the 3rd missing element is 6.



Input: a = [2, 3, 5], n = 5


Output: 'Does not exist'

Since there is no 5th missing element in the array, we output 'Does not exist' (the only missing element here is 4).
"""