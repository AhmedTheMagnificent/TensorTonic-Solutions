import numpy as np

def vgg_maxpool(x: np.ndarray) -> np.ndarray:
    """
    Implement VGG-style max pooling (2x2, stride 2).
    """
    # Your implementation here
    pass
    N, H, W, C = x.shape
    x = x.reshape(N, H // 2, 2, W // 2, 2, C)
    x = x.max(axis=(2, 4))
    return x