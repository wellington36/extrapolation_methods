import math
import numpy as np
from acceleration import *
from configuration import *

import matplotlib.pyplot as plt
import time

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
    e = 0.10
    max_steps = 1

    print(constants[3])
    for t in [no_transform, Aitken_transform, Richardson_transform, Epsilon_transform, G_transform]:
        
        if t in [G_transform]:
            continue
        print(f"########## {e} ##########")
        t0 = time.time()
        n, acel = acceleration(slow_series, transform=t, error=e, max_steps=max_steps)
        t1 = time.time()

        print(f"{t.__name__}    |   {t1-t0} |   {acel[-1]}  |   {n}")

        plt.plot(range(len(acel))[30:], acel[30:], label=t.__name__)
    
    plt.legend()
    plt.show()
