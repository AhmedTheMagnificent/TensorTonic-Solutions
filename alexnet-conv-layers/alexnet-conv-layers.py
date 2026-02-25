import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    F = 96
    S = 4
    N, H, W, C = image.shape
    out_H = (H - 11) // S + 2 
    out_W = (W - 11) // S + 2
    return np.zeros((N, out_H, out_W, F))