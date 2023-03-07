import math
import numpy as np
from acceleration import Aitken_transform, Aitken_transform_m, Richardson_transform, Richardson_transform_m, Epsilon_transfom, G_transform
from configuration import *

def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, converges to math.pi**2 / 6"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

def zeta(n: int, s: float) -> np.ndarray:
    """Zeta function"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**s

    return series

def dirichlet_series(n: int) -> np.ndarray:
    """Dirichlet series, converges to math.log(2)"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + (-1)**i * 1/(i+1)

    return series


if __name__ == "__main__":
    STEPS = 1
    N = 1_000_000
    p = 2

    print(math.pi**2 / 6)
    print(zeta(N, p)[-1])
    #print(Aitken_transform(zeta(N, p), steps=STEPS)[-1])
    print(Aitken_transform_m(square_series, error=1e-6)[-1])
    #print(Richardson_transform(zeta(N, p), steps=STEPS)[-1])
    #print(Richardson_transform_m(square_series, error=1e-6)[-1])
    #print(Epsilon_transfom(zeta(N, p), steps=-1)[-1])
    #print(G_transform(zeta(N, p), steps=STEPS)[-1])
