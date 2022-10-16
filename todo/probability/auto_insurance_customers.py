"""
An insurance company classifies its customers into 3 categories: below average, average, and above average. No one moves more than one state at a time.

For example, a customer cannot move from below average to above average or from above average to below average in a given period. After a given period, we notice that:

40% of those in the below average category become average
30% of those in the average category become above average
10% of those in the average category become below average
20% of those in the above average category are downgraded to average
Given the above:

Can you write the transition matrix for the model?
What is the limiting fraction of drivers in each of these categories? (e.g. find the steady state)
Hint: It might be helpful to start with building a state transition diagram to depict a Markov chain for the different states a customer can move to given their current state.
"""