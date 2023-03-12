import math
import numpy as np
from acceleration import *
from configuration import *

def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, converges to math.pi**2 / 6"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**(2)
    
    return series

def slow_zeta_series(n: int) -> np.ndarray:
    """Zeta(1.2) series, converges to z (in the other file)"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**(1.2)
    
    return series

def dirichlet_series(n: int) -> np.ndarray:
    """Dirichlet series, converges to math.log(2)"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + (-1)**i * 1/(i+1)

    return series


if __name__ == "__main__":
    e = 1e-3

    print(math.pi**2/6)
    print(acceleration(square_series, no_transform, e)[-1])
    print(acceleration(square_series, Aitken_tranform, e)[-1])
    print(acceleration(square_series, Richardson_transform, e)[-1])
    print(acceleration(square_series, Epsilon_transform, e)[-1])
    print(acceleration(square_series, G_transform, e)[-1])
