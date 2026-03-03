import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points = np.array(points)
    singlePoint = False
    if points.ndim == 1:
        points = points.reshape(1, 3)
        singlePoint = True
    ones = np.ones((points.shape[0], 1))
    points = np.hstack((points, ones))
    transformed = (T @ points.T).T
    if singlePoint:     
        return transformed[0, :3]
    return transformed[:, :3]
    