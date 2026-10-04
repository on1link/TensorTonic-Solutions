import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    
    upper = np.vdot(a,b)
    low = np.linalg.norm(a) * np.linalg.norm(b) + 1e-07
    if low == 0:
        return 0.0
    return float(upper/low)