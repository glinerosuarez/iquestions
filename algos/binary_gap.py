"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both
ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no
binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N
doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure
prohibited.
"""

def solution(N):
    # write your code in Python 3.6
    start_count = False
    max_count = 0
    buffer = 0

    for bit in "{0:b}".format(N):
        bit = int(bit)
        if bit and start_count is False:
            start_count = True
        elif bit and start_count:
            # Gap found!
            if buffer > max_count:
                max_count = buffer
            buffer = 0
        elif bit == 0 and start_count:
            buffer += 1
        else:
            continue

    return max_count


if __name__ == '__main__':
    assert solution(1041) == 5
