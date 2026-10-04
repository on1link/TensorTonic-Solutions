import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    
    def _negative_sigmoid(v):
        return np.exp(v) / (1 + np.exp(v))

    def _positive_sigmoid(v):
        return 1 / (1 + np.exp(-v))

    x = np.asarray(x, dtype=float)

    positive = x >= 0
    negative = ~positive
    res = np.empty_like(x, dtype=float)
    res[positive] = _positive_sigmoid(x[positive])
    res[negative] = _negative_sigmoid(x[negative])

    return res.item() if x.ndim == 0 else res
    