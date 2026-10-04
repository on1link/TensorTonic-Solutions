import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """

    X = np.asarray(X, dtype=float)

    mean = np.mean(X, axis=0)
    X_c = X - mean

    cov = (X_c.T @ X_c) / (X_c.shape[0] - 1)

    return cov