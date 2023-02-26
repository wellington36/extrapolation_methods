import math
import numpy as np
from acceleration import Aitken_tranform, Richardson_transform, Epsilon_transfom, G_transform

# SET DATA TYPE
DT = np.dtype('float64') # float 64 bits

def square_series(n: int) -> np.ndarray:
    series = np.zeros(n, dtype=DT)
    series[0] = 1

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

if __name__ == "__main__":
    for i in range(1, 6):
        initial_series = abs(math.pi**2 / 6 - square_series(10**i)[-1])
        acceration_series = abs(math.pi**2 / 6 - Aitken_tranform(square_series(10**i))[-1])

        print(f"Error in initial series with n={10**i}: {initial_series}")
        print(f"Errro in acceleration series with n={10**i}: {acceration_series}")
        print("\n")

    print(Epsilon_transfom(square_series(10)))

    #print(math.pi**2 / 6)
    #print(square_series(10000)[-1])
    #print(Aitken_tranform(np.array(square_series(10000)), 10)[-1])
