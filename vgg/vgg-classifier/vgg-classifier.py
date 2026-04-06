import numpy as np

def vgg_classifier(features: np.ndarray, num_classes: int = 1000) -> np.ndarray:
    """
    Implement VGG's fully connected classifier.
    """
    # Your implementation here
    if features.ndim == 4:
        N, W, H, C = features.shape
        x = features.reshape(N, -1)
    else:
        x = features
    D = x.shape[1]
    
    w1 = np.random.randn(D, 4096) * 0.01
    b1 = np.zeros(4096)
    x  = np.maximum(0, x @ w1 + b1)

    w2 = np.random.randn(4096, 4096) * 0.01
    b2 = np.zeros(4096)
    x  = np.maximum(0, x @ w2 + b2)

    w3 = np.random.randn(4096, num_classes) * 0.01
    b3 = np.zeros(num_classes)
    z  = x @ w3 + b3

    return z

    