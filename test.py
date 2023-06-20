import math
import numpy as np
from src.acceleration import *
from src.configuration import *
import matplotlib.pyplot as plt
import time

###### series ######
def basel_series(n: int):
    return 1/(n)**2

def slow_series(n: int):
    return 1/((n+1)*(math.log(n+1))**2)

def dirichlet_series(n: int) -> float:
    if n == 1:
        return 1.0
    return (-1)**n/(n+1)


###### test acceleration ######
if __name__ == "__main__":
    e = 1e-6

    print(constants[1]**2/6)
    for t in [no_transform, Aitken_transform, Richardson_transform, Epsilon_transform, G_transform]:
        
        if t in [Aitken_transform, Epsilon_transform, G_transform, no_transform]:
            continue

        print(f"########## {e} ##########")
        t0 = time.time()
        
        n, acel = acceleration(basel_series, transform=t, error=e)
        t1 = time.time() - t0

        t0 = time.time()
        n, acel = acceleration(basel_series, transform=t, error=e)
        t2 = time.time() - t0

        t0 = time.time()
        n, acel = acceleration(basel_series, transform=t, error=e)
        t3 = time.time() - t0

        print(f"{t.__name__}    |   {(t1 + t2 + t3) / 3} |   {acel[-1]}  |   {n}")

        #plt.plot(range(len(acel)), acel, label=t.__name__)
    
    #plt.legend()
    #plt.show()