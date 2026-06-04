import numpy as np

def kl_divergence(mu: np.ndarray, log_var: np.ndarray) -> float:
    """
    Returns: float scalar KL divergence averaged over the batch
    """
    # Your implementation here
    D_kl =  - 1 / 2 * (np.sum(1 + log_var - mu ** 2 - np.exp(log_var), axis=1))
    return np.mean(D_kl)