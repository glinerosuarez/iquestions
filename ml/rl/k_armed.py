import numpy as np


n_arms = 10
methods = [0, 0.1, 0.01]
T = 1_000
Q = np.zeros((n_arms, 3))
q_star = np.random.normal(size=n_arms)


def run(epsilon):
    for _ in range(T):
        # Pick an action
        if np.random.uniform() >= epsilon:
            A = np.argmax(Q[:, 2])
        else:
            A = np.random.choice(np.arange(n_arms))

        # Get a reward
        R = np.random.normal(q_star[A])

        # Update our table
        Q[A][0] = Q[A][0] + R        # Cumulative reward
        Q[A][1] = Q[A][1] + 1        # Number of times this action has been taken
        Q[A][2] = Q[A][0] / Q[A][1]  # Avg reward


if __name__ == '__main__':
    run(0.1)
    print(q_star)
    print(Q[:, 2])