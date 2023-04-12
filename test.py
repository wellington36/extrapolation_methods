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
    e = 1e-4
    steps = 1

    print(constants[1]**2/6)
    for t in [no_transform, Aitken_transform, Richardson_transform, Epsilon_transform, G_transform]:
        
        if t in []:
            continue

        print(f"########## {e} ##########")
        t0 = time.time()
        n, acel = acceleration(square_series, transform=t, error=e, max_steps=steps)
        t1 = time.time() - t0

        t0 = time.time()
        n, acel = acceleration(square_series, transform=t, error=e, max_steps=steps)
        t2 = time.time() - t0

        t0 = time.time()
        n, acel = acceleration(square_series, transform=t, error=e, max_steps=steps)
        t3 = time.time() - t0

        print(f"{t.__name__}    |   {(t1 + t2 + t3) / 3} |   {acel[-1]}  |   {n}")

        plt.plot(range(len(acel))[20:], acel[20:], label=t.__name__)
    
    plt.legend()
    plt.show()
