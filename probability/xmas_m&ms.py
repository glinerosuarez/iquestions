"""
Suppose you have two different bags of M&Ms, one is a special Christmas edition while the other is a standard bag of
M&Ms. The Christmas edition contains only red, green, and white M&Ms while the standard bag contains the full color
offering. The distributions of drawing a given color are below:

Christmas bag of M&Ms

Green: 30%
Red: 40%
White: 30%
Standard bag of M&Ms

Green: 20%
Orange: 19%
Blue: 19%
Red: 15%
Yellow: 14%
Brown: 13%
You are given an M&M from each bag, but you do not know which M&M came from which bag. One M&M is Red and one is Green.
What is the probability that the Red M&M came from the Standard bag?
"""
import numpy as np


def empiric_sol(samples):
    xmas_bag = np.random.choice([1, 0], samples, p=[.4, .6])
    stndrd_bag = np.random.choice([1, 0], samples, p=[.15, .85])
    table = np.hstack([np.expand_dims(xmas_bag, 1), np.expand_dims(stndrd_bag, 1)])
    table = np.hstack([table, np.expand_dims(table[:, 0] + table[:, 1], 1)])
    red_outcomes = table[table[:, 2] == 1]
    xmas_p = red_outcomes[:, 0].sum() / len(red_outcomes)
    stndrd_p = red_outcomes[:, 1].sum() / len(red_outcomes)
    #print(table, "\n")
    #print(red_outcomes)
    print(len(red_outcomes))
    print(f"prob from xmas: {xmas_p}, prob from standard: {stndrd_p}")


def bayes_sol():
    # Bayes theorem: P(A|B) = P(B|A) * P(A) / P(B)
    # So, P(A|B) is the probability that the M&M came from the standard bag given that it's red.
    # P(A) is the probability of coming from the standard bag.
    # P(B) is the probability of being red.
    # And P(B|A) is the probability of being red given that it's coming from the standard bag.
    # Since we know that we get 1 m&m from each bag, For P(A) the probability is 0.5
    p_A = .5
    # For P(B) two are three possible outcomes that meet the criteria: red - different color, different color - red.
    # We sum up these probabilities:
    p_B = .4*.85 + .6*.15
    # The probability of picking a red m&m from the standard bag is given to us.
    p_BA = .15
    # Replace and find the result:
    p_AB = p_BA * p_A / p_B

    return p_AB


if __name__ == '__main__':
    print(bayes_sol())
    #print(empiric_sol(10_000_000))



