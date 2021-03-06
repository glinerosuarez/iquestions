"""
You go to see the doctor about a cough you've had for a while. The doctor selects you at random to have a blood test for
a new strain of flu, which for the purposes of this exercise we will say is currently suspected to affect 1 in 10,000
people in the US. The test is 99% accurate, in the sense that the probability of a false positive is 1%. The probability
of a false negative is zero. You test positive. What is the new probability that you have this strain of flu?
"""
if __name__ == '__main__':

    flu_prop = 1 / 10_000
    test_acc = 0.99
    false_positive = 0.01
    false_negative = 0.0

    # A having the flu
    # B tested positive

    # bayes P(A | B) = [P(B | A) . P(A)] / P(B)
    pA = flu_prop
    pB = flu_prop + false_positive*(1 - flu_prop)
    pBA = 1
    pAB = (pBA * pA) / pB
    print(f"{pAB:0.2%}")
