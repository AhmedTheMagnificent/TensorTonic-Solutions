import numpy as np

def reverse_step(x_t, t, epsilon_pred, betas, z=None):
    """
    Returns: np.ndarray x_{t-1} after one reverse diffusion step
    """
    # YOUR CODE HERE
    x_t = np.array(x_t)
    epsilon_pred = np.array(epsilon_pred)
    betas = np.array(betas)
    alpha_bar = np.cumprod(1 - betas)[t - 1]
    
    x = 1 / np.sqrt(1 - betas[t - 1]) * (x_t - betas[t - 1] / np.sqrt(1 - alpha_bar) * epsilon_pred)
    if z is not None:
        z = np.array(z)
        x += np.sqrt(betas[t - 1]) * z
    return x