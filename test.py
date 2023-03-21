import math
import numpy as np
from acceleration import *
from configuration import *
import matplotlib.pyplot as plt

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

def slow_series(n: int) -> np.ndarray:
    series = np.zeros(n, dtype=DT)
    series[0] = 1/(2*(math.log(2))**2)

    for i in range(1, n):
        series[i] =  series[i-1] + 1/((i+2)*(math.log(i+2))**2)
    
    return series


if __name__ == "__main__":
    e = 0.12
    max_steps = 1

    print(constants[3])
    for i in np.arange(0.13, 0.08, -0.01):
        print(acceleration(slow_series, no_transform, i, max_steps=max_steps)[-1])
        print(acceleration(slow_series, Aitken_transform, i, max_steps=max_steps)[-1])
        print(acceleration(slow_series, Richardson_transform, i, max_steps=max_steps)[-1])
        print(acceleration(slow_series, Epsilon_transform, i, max_steps=max_steps)[-1])
        print(acceleration(slow_series, G_transform, i, max_steps=max_steps)[-1])
