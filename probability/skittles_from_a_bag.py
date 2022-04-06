"""
A bag contains 40 skittles: 16 yellow, 14 red, and 10 orange. You draw 3 skittles at random (without replacement) from
the bag. What is the probability that you get 2 skittles of one color and another skittle of a different color?
"""


def compute_scenario(equal: str):
    skittles = dict(y=16, r=14, o=10)
    others = sum([v for k, v in skittles.items() if k != equal])
    equal = skittles[equal]
    total = others + equal
    return (equal / total) * ((equal - 1) / (total - 1)) * (others / (total - 2))


if __name__ == '__main__':
    print(compute_scenario("y") + compute_scenario("r") + compute_scenario("o"))
