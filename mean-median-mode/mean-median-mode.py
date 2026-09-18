from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    u, c = np.unique(x, return_counts=True)   

    mode = float(u[np.argmax(c)])
    return {'mean': float(np.mean(x)), 'median': float(np.median(x)), 'mode': mode}