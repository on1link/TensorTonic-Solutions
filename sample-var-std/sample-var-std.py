import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x)
    variance =  np.sum((x - x.mean())**2) / (x.shape[0] - 1)
    std = np.sqrt(variance)
    return  {"variance":float(variance), "standard_deviation": float(std)}
