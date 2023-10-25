# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
use hash sets to keep track of numbers seen in rows, columns and squares

# Approach
<!-- Describe your approach to solving the problem. -->
use hash sets to keep track of numbers seen in rows, columns and squares

# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rseen = set()
        cseen = set()
        qseen = set()

        for i, r in enumerate(board):
            for c, n in enumerate(r):
                if n == ".":
                    continue
                q = str(i // 3) + str(c // 3)
                nr, nc, nq = (n + str(i)), (n + str(c)), (n + q)
                if (
                    nr in rseen
                    or nc in cseen
                    or nq in qseen
                ):
                    return False
                else:
                    rseen.add(nr)
                    cseen.add(nc)
                    qseen.add(nq)
    
        return True
                    


```