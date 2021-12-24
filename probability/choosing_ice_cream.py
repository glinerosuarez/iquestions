"""
Suppose you enter an ice cream store. They sell two types of ice cream: soft serve and frozen yogurt. Additionally,
there are 10 flavors of soft serve and 13 flavors of frozen yogurt. You're really hungry, so you decide you can order
and eat two ice creams before they melt, but are facing some decision fatigue given the amount of choices.
How many ways are there to choose exactly two ice creams from the store? Figuring this out should help quantify that
decision fatigue.
"""

if __name__ == '__main__':
    types = ["soft serve", "frozen yogurt"]
    soft_flavors = 10
    yogurt_flavors = 13
    total_flavors = soft_flavors + yogurt_flavors


    def factorial(n: int) -> int:
        """Compute the factorial of a number."""
        if n in [0, 1]: return 1
        return n * factorial(n - 1)

    def comb_without_repetition(n: int, k: int) -> int:
        """
        Combinations without repetition.
        :param n: possibilities
        :param k: taken
        :return: number of combinations
        """
        return factorial(n)/(factorial(k)*factorial(n - k))

    print(comb_without_repetition(total_flavors, 2))
