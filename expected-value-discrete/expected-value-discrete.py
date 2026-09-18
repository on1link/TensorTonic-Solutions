import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    expected_value = 0
    for i in range(len(x)):
        expected_value += x[i] * p[i]
        
    return float(expected_value)