"""
InterviewQs
Biased coin toss
Suppose you want to generate a sample of heads and tails from a fair coin. However, you only have a biased coin
available (meaning the probability of coming up with heads is different than 1/2).

Write a simulation in Python that will use your biased coin to generate a sample of heads/tails as if it were coming
from a fair coin.

Solution:

We need to create a system which returns heads and tails with equal probability. Let us define an event as flipping
the unfair coin twice and compute the probability of all possible results, given that the probability of getting a 
heads when tossing the unfair coin is equal to p, then:
1) Heads and Heads = 2p
2) Tails and Tails = (1 - p)(1 - p)
3) Heads and Tails = p(1 - p)
4) Tails and Heads = (1 - p)p = p(1 -p)

3 and 4 have the same probability, thus we can keep flipping the unfair coin until we reach any of these two states and
return the first result to decide the outcome. In other words, for 3 our function will return Heads whereas for 4 our
function will return Tails.

We can prove that the probability of returning Heads or Tails in our system is equal to 0.5 by applying Bayes Theorem.
For two events A and B:
P(A|B) = ( P(A)P(B|A) )/P(B)

In our system, A is the probability of getting Heads in the first flip and B is the probability of getting different coin 
sides, so P(A|B) is the probability of getting Heads in the first flip given that both flips result in different results
, therefore:
P(A) = p
P(B) = 2p(1 - p)
P(B|A) = (1 - p)

P(A|B) = ( p*(1 - p) )/2p(1 - p) = p/2p = 1/2

"""
import enum
import numpy as np
import scipy.stats
from typing import Tuple, List


class CoinToss(enum.IntEnum):
    TAILS = 0
    HEADS = 1


def unfair_coin_toss() -> CoinToss:
    p = .75  # This value must be 0 < p < 1
    return np.random.choice(list(CoinToss), p=[1 - p, p])


def toss_unfair_coin_twice() -> Tuple[CoinToss, CoinToss]:
    return unfair_coin_toss(), unfair_coin_toss()


def fair_coin_toss() -> CoinToss:
    first, second = toss_unfair_coin_twice()
    while first == second:
        first, second = toss_unfair_coin_twice()
    return first


def sample_from_fair_empirical(size: int) -> np.array:
    return np.array([fair_coin_toss() for _ in range(size)])


def sample_from_fair_reference(size: int) -> List[CoinToss]:
    p = .5
    return np.random.choice(list(CoinToss), size, p=[1 - p, p])


def chi_squared_test(size: int = 100):
    # Compute observation frequencies.
    _, obs_f = np.unique(sample_from_fair_empirical(size), return_counts=True)
    # Compute expected frequencies.
    exp_f = size * np.array([.5, .5])
    # Compute statistic with k-1 degrees of freedom where k is the number of categories(2).
    x2 = np.sum(np.square(exp_f - obs_f)/exp_f)
    # Fin chi squared probability
    p = scipy.stats.chi2.sf(x2, df=1)
    # Check if we can reject h0
    return p


if __name__ == '__main__':
    print("generating 10 fair toss with an unfair coin:")
    print([CoinToss(fair_coin_toss()) for _ in range(10)])
    print("conducting Chi-Squared test with 10.000 examples:")
    p = chi_squared_test(10_000)
    print(f"since p = {round(p, 4)} we {'cannot' if p > .05 else 'can'} reject the null hypothesis that the samples "
          f"come from a fair coin ")
