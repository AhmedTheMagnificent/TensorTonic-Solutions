import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True) -> np.ndarray:
    """Apply dropout to input."""
    # YOUR CODE HERE
    return np.random.binomial(1, 1-p, x.shape) * x * (1 / (1 - p)) if training else x