"""
Given an integer matrix, m, with an odd # dimensions, n x n, (e.g 3 x 3, 5 x 5, etc), find the sum of middle row as well
as the middle column.

For example:
#Given
[[1,2,3],
[4,5,6],
[7,8,9]]

#Your program would output:
'Sum middle row =' 15 #(e.g. 4+5+6)
'Sum middle column =' 15 #(e.g. 2+5+8)
"""
def solution(a):
    n = len(a)
    middle = int(n/2)

    print(f'Sum middle row = {sum(a[middle])}')
    print(f'Sum middle column = {sum([a[i][middle] for i in range(n)])}')


if __name__ == '__main__':
    solution([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
