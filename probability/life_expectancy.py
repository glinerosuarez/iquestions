"""
Suppose you're analyzing a population of 100,000 people, and you're trying to understand life expectancy. Within this
population of 100,000 people, 75% can expect to live to the age of 70, while 45% can expect to live to age 80. Given
that a person is 70, what is the probability that they live to the age 80?
"""

if __name__ == '__main__':
    population = 100_000
    live_to_70 = .75
    live_to_80 = .45

    # P(A|B) = P(B|A) . P(A) / P(B)
    # P(B|A) is probability to live to 70 given that the person is 80
    p_BA = 1
    # P(A) probability to live to 80
    p_A = live_to_80
    # P(B) probability to live to 70
    p_B = live_to_70

    p_AB = p_BA * p_A / p_B
    print(p_AB)