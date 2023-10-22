# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
recursion, iterate over the list

# Approach
<!-- Describe your approach to solving the problem. -->
recursion: variable to keep track of the tail of the list (new head) treat evey iteration as the new head.
iterative: for every iteration we have the variables prev, curr and head.next to do the swap.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$
$$O(n)$$

# Code
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            
        return new_head        
```