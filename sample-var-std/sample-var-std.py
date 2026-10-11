import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x)
    variance =  np.sum((x - np.mean(x))**2) / (x.size - 1)
    std = np.sqrt(variance)
    return  {"variance":float(variance), "standard_deviation": float(std)}
