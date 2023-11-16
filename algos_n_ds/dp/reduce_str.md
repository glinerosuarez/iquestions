# Problem
Given a string of any combination of three letters ‘a’, ‘b’, and ‘c’, find length of the smallest string that can be obtained by applying the following operation repeatedly: 

Take any two adjacent, distinct characters and replace them with the third.

Examples:
Input : cab
Output : 2
We can select any two adjacent letters, 
say 'ca' and transform it into 'b', this 
leaves us with string 'bb' of length two.
    
Input : bcab
Output : 1
Selecting 'bc' and transforming it to 'a' 
leaves us with 'aab'. We can then select
'ab' and transform it to 'c', giving 'ac'. 
This can further be transformed into 'b',
which is of length one.

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
If the string cannot be reduced further, then all letters in the string are the same.
The length of minimum string is either <= 2 or equal to the length of original string, or 2 < minimum string length < original string length is never true.
If each letter of the string is present an odd amount of times, after one reduction step, they shall all be present an even amount of times. The converse is also true, that is, if each letter of the string is present an even amount of times, they shall be present an odd amount of times after one reduction step.
These can be proven as follows: 

If any two different letters are present, we can select these and reduce string length further.
Proof by contradiction: 
Assume we have a reduced string of length less than original string. For example ‘bbbbbbb’. Then this string must have originated from a string like ‘acbbbbbb’, ‘bbacbbbb’ or any other such combination of the same. In this case, we could have selected ‘bc’ instead of ‘ac’ and reduced further.
From the recursive step above, we increase one letter by one and decrease the other two by one. So if we had a combination as (odd, odd, odd), then it would become (odd + 1, odd – 1, odd – 1) or (even, even, even). The reverse is shown in a similar fashion.

# Approach
<!-- Describe your approach to solving the problem. -->
Now we can combine the above principles. 
If the string consists of the same letter repeating, it’s minimum reduced string is itself, and length is the length of the string. 
Now, the other possible options are reduced string being of one character length or two. Now if all characters are present an even number of times, or an odd number of times, the only answer that is possible is 2, because (0, 2, 0) is (even, even, even) while (0, 1, 0) is (even, odd, even) so only 2 preserves this evenness. 
In any other condition, the answer becomes 1.  

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```
def stringReduction(str):
 
    n = len(str)
 
    # Counint occurrences of three different
    # characters 'a', 'b' and 'c' in str
    count = [0] * 3
    for i in range(n):
        count[ord(str[i]) - ord('a')] += 1
 
    # If all characters are same.
    if (count[0] == n or count[1] == n or
                         count[2] == n):
        return n
 
    # If all characters are present even number
    # of times or all are present odd number of
    # times.
    if ((count[0] % 2) == (count[1] % 2) and
        (count[1] % 2) == (count[2] % 2)):
        return 2
 
    # Answer is 1 for all other cases.
    return 1
```