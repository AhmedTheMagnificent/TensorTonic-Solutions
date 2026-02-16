def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    T = len(rewards)
    returns = [0] * T
    returns[T - 1] = rewards[T - 1]
    for t in reversed(range(T - 1)):
        returns[t] = rewards[t] + gamma * returns[t + 1]
    return returns
    