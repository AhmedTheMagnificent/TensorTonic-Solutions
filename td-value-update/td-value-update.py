import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    target = r + gamma * V[s_next]
    error = target - V[s]
    V[s] += alpha * (error)
    return V