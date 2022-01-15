"""
A given car has a number of miles it can run before its battery is depleted, where the number of miles are exponentially
distributed with an average of 10,000 miles to depletion.
If a given individual needs to make a trip that's 3,000 miles, what is the probability that she/he will be able to
complete the trip without having to replace the battery? You can assume the car battery is new for this problem.
"""
import math


def exp_cdf(decay, x):
    return 1 - math.e**(-decay*x)


if __name__ == '__main__':
    avg = 10_000  # Average to battery depletion
    trip_length = 3_000  # miles

    decay_param = 1 / avg
    p_trip = 1 - exp_cdf(decay_param, 3000)
    print(p_trip)
