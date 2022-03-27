"""In a particular area, there are 2 types of weather: sunny and rainy. The following is observed across a couple year
period.
The probability of weather staying sunny the following week is 80%.
The probability of the weather changing from sunny to rainy is 20%.
The probability of the weather staying rainy from the following week is 70%.
The probability of weather changing from rainy to sunny over a week is 30%.
Given this information, can you create a transition matrix and calculate the steady state vector?
"""
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)

if __name__ == '__main__':
    states = ["sunny", "rainy"]
    probs = [
        [.8, .2],
        [.3, .7]
    ]
    transition_matrix = pd.DataFrame(probs, index=states, columns=states)
    I_minus_p = np.eye(2) - transition_matrix.values
    equation_sys = np.hstack([np.vstack([I_minus_p[:, 0], [1, 1]]), np.expand_dims([0, 1], 1)])
    # Use row-reduction to find values
    equation_sys = equation_sys * 10
    # -5*R1 + R2 -> R2
    equation_sys[1] = -5*equation_sys[0] + equation_sys[1]
    # R2/25 -> R2
    equation_sys[1] = equation_sys[1] / 25
    # 3R2 + R1 -> R1
    equation_sys[0] = 3*equation_sys[1] + equation_sys[0]
    # R1/2 -> R1
    equation_sys[0] = equation_sys[0]/2
    solution = equation_sys[:, -1]
    print(solution)