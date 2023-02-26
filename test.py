import math
import numpy as np
from acceleration import Aitken_tranform, Richardson_transform, Epsilon_transfom, G_transform

# SET DATA TYPE
DT = np.dtype('float64') # float 64 bits

def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, sum of math.pi**2 / 6"""
    series = np.zeros(n, dtype=DT)
    series[0] = 1

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

if __name__ == "__main__":
    print(math.pi**2 / 6)
    print(square_series(10000)[-1])
    print(G_transform(np.array(square_series(10000)), steps=100)[-1])
