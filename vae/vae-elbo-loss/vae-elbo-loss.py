import numpy as np

def vae_loss(x: np.ndarray, x_recon: np.ndarray, mu: np.ndarray, log_var: np.ndarray) -> dict:
    """
    Returns: dict with "total", "recon", and "kl" loss values as floats
    """
    # Your implementation here
    reconstruction_loss = np.mean(np.sum((x - x_recon) ** 2, axis=1) )
    regularization_loss = np.mean(- 0.5 * np.sum(1 + log_var - mu ** 2 - np.exp(log_var), axis=1))
    return {
        "total": reconstruction_loss + regularization_loss,
        "recon": reconstruction_loss,
        "kl": regularization_loss
    }