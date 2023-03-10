import math
import numpy as np
from acceleration import *
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
    e = 0.01229482

    print(math.pi**2 / 6)
    #print(abs(square_series(999)[-1] - math.pi**2 / 6) < e)
    print(no_transform(square_series, error=e)[-1])
    #print(Aitken_transform(square_series, error=e)[-1])
    #print(Richardson_transform(square_series, error=e)[-1])
    #print(Epsilon_transform(square_series, error=e)[-1])
    #print(G_transform(square_series, error=e)[-1])
