# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
split list into two halves

# Approach
<!-- Describe your approach to solving the problem. -->
split list into two halves, reverse second half, merge two halves

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split link into two halves using slow fast pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        head2 = slow.next
        slow.next = None
        curr, prev = head2, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head2 = prev

        # Merge halves
        while head2:
            next_head = head.next
            head.next = head2
            head2 = head2.next
            head.next.next = next_head
            head = next_head
            

```