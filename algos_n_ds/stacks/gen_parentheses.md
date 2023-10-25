# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
explore all combinations
# Approach
<!-- Describe your approach to solving the problem. -->
use recursion avoiding invalid combinations

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
Time Complexity (Big O): O(2^(2n) / sqrt(n))

The time complexity is dominated by the number of valid combinations generated. In the worst case, there can be 2^(2n) valid combinations of parentheses. However, this solution uses a pruning technique that prevents generating invalid combinations. The backtrack function will not explore paths that lead to invalid combinations, which reduces the number of recursive calls. The exact time complexity is difficult to express precisely due to the pruning, but it's often approximated as O(2^(2n) / sqrt(n)).

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
Space Complexity (Big O): O(2n)

The space complexity is determined by the maximum depth of the recursion stack. In this case, the recursion depth can go up to 2n, where n is the number of pairs of parentheses. Therefore, the space complexity is O(2n).

Keep in mind that the actual time and space usage can vary based on factors like the Python interpreter's implementation and optimizations, but the provided complexities are reasonable approximations for most practical cases.

# Code
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        max_length = n * 2
        result = []
        
        def get_comb(base, open, close):
            if open + close == max_length:
                result.append(base)
            else:
                if open == n:
                    get_comb(base + ")", open, close + 1)
                elif open - close > 0:
                    get_comb(base + "(", open + 1, close)
                    get_comb(base + ")", open, close + 1)
                else:
                    get_comb(base + "(", open + 1, close)

        get_comb("(", 1, 0)

        return result
        
```