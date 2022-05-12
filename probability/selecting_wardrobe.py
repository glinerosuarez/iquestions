"""
Suppose Charlie has 3 pairs of shoes, 4 different coats, and 2 different pants to wear in his wardrobe. Of those items,
Charlie has exactly one pair of white shoes, exactly one black coat, and exactly one pair of khaki pants. If Charlie
selects each item of his wardrobe at random, what is the probability that he will wear the white shoes, black coat, and
khaki pants?
"""
if __name__ == '__main__':
    shoes_pairs = 3
    coats = 4
    pants = 2

    # first pick
    p1 = 3 / (shoes_pairs + coats + pants)
    # second pick
    p2 = 2 / (shoes_pairs + coats + pants - 1)
    # third pick
    p3 = 1 / (shoes_pairs + coats + pants - 2)

    print(p1 * p2 * p3)
