import math
import numpy as np
from acceleration import Aitken_transform, Richardson_transform, Epsilon_transfom, G_transform
from configuration import *

def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, converges to math.pi**2 / 6"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

def dirichlet_series(n: int) -> np.ndarray:
    """Dirichlet series, converges to math.log(2)"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + (-1)**i * 1/(i+1)

    return series


if __name__ == "__main__":
    N = 10_000

    print(math.pi**2 / 6)
    print(square_series(N)[-1])
    print(Aitken_transform(square_series, error=1e-10)[-1])
    print(Richardson_transform(square_series, error=1e-10)[-1])
    print(Epsilon_transfom(square_series(N), steps=10)[-1])
    print(G_transform(square_series(N), steps=10)[-1])
