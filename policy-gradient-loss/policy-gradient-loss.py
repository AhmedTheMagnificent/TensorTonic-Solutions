def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    # Write code here
    T = len(log_probs)
    G = [0 for _ in range(T)]
    for t in reversed(range(T)):
        G[t] = rewards[t] + gamma * G[t + 1] if t + 1 < T else rewards[t]
    G_mean = sum(G) / T
    advantege = [g - G_mean for g in G]
    loss = -sum(a * lp for a, lp in zip(advantege, log_probs)) / T
    return loss