# -*- coding: utf-8 -*-
"""
Suppose you're working in a parts manufacturing plant, and you're running quality analysis on the gasket 
production line. Gaskets produced by your company will be defective 1% of the time, and are distributed to 
customers in packs of 20. Your company has a policy where if 2 or more of the 20 gaskets in a given pack is 
defective, they will replace the entire package for free. What proportion of packages does the company need 
to replace?
"""

import math
from scipy.stats import binom

def binomial_func(n, x, p):
    nCx = math.factorial(n)/(math.factorial(x) * math.factorial(n - x))
    return nCx * p**x * (1 - p)**(n - x)

p = 0.01
n = 20
# P(x>1) = 1 - P(x=0) - P(x=1)
P = 1 - binomial_func(20, 0, p) - binomial_func(20, 1, p)
print(f"{P:0.2%}")

print(f"{1 - binom.pmf(0, n, p) - binom.pmf(1, n, p):0.2%}")

print(f"{1 - binom.cdf(1, n, p):0.2%}")

