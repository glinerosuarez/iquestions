"""
A fair coin is tossed repeatedly and independently. Find the expected number of tosses until the pattern Head-Tail-Head
appears.

Hint: It might be helpful to start with building a state transition diagram to depict a Markov chain for the coin toss.
"""
import numpy as np

if __name__ == '__main__':
    """
    First we build P
        T   H   HT  HTH
    T   0.5 0.5 0   0   
    H   0   0.5 0.5 0
    HT  0.5 0   0   0.5
    HTH 0   0   0   1
    
    from the canonical form we get Q:
        T   H   HT  
    T   0.5 0.5 0     
    H   0   0.5 0.5
    HT  0.5 0   0   
    """
    Q = np.array([
        [.5, .5, 0],
        [0, .5, .5],
        [.5, 0, 0],
    ])
    """
    and I - Q is:
        T    H    HT  
    T   0.5  -0.5 0     
    H   0    0.5  -0.5
    HT  -0.5 0    1       
    """
    I_Q = np.eye(3) - Q
    """
    now we compute the inverse of (I - Q) which is called the fundamental matrix of P denoted by N
        T H HT  
    T   4 4 2    
    H   2 4 2
    HT  2 2 2      
    """
    N = np.linalg.inv(I_Q)
    """
    Now we compute the time to absorption from the transition states t = Nc where c is a column vector of ones
    """
    t = N @ np.ones(len(N))
    """
    We are interested in the expected number of steps from the initial state
    """
    print(f"Answer: {t[0]}")