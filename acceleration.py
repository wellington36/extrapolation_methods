import math
import numpy as np
from configuration import *

def Aitken_transform(series, error=1e-5) -> np.ndarray:
    n = 4   # initial value
    acel = np.zeros(n-2, dtype=DT)
    s = series(n) # series of n elements (np.array)

    for i in range(0, n-2):
        acel[i] = (s[i] * s[i+2] - s[i+1]**2) / \
            (s[i+2] - 2 * s[i+1] + s[i])
    
    while abs(acel[-1] - acel[-2]) > error:
        n += 1  # step to find the best solution
        acel = np.zeros(n-2, dtype=DT)
        s = series(n) # series of n elements (np.array)

        for i in range(0, n-2):
            acel[i] = (s[i] * s[i+2] - s[i+1]**2) / \
                (s[i+2] - 2 * s[i+1] + s[i])
    
    #print(n)
    return acel

def Richardson_transform(series, p=1, error=1e-5) -> np.ndarray:
    n = 4   # initial value
    acel = np.zeros(int(n/2), dtype=DT)
    s = series(n) # series of n elements (np.array)

    for i in range(0, int(n/2)):
        acel[i] = s[2*i] + (s[2*i] - s[i]) / \
            np.expm1(p * math.log(2))
    
    while abs(acel[-1] - math.pi**2/6) > error:
        n += 1  # step to find the best solution
        acel = np.zeros(int(n/2), dtype=DT)
        s = series(n)

        for i in range(0, int(n/2)):
            acel[i] = s[2*i] + (s[2*i] - s[i]) / \
                np.expm1(p * math.log(2))
    
    #print(n)
    return acel

def Epsilon_transform(series, error=1e-5) -> np.ndarray:
    n = 4   # initial value
    s = series(n)
    acel = s
    aux = np.zeros(n+1, dtype=DT)

    while abs(acel[-1] - acel[-2]) > error:
        n += 1
        s = series(n)
        acel = s
        aux = np.zeros(n + 1, dtype=DT)

        for i in range(0, len(aux) - 3):
            aux[i] = acel[i+1] + 1/(acel[i+1] - acel[i])
        aux = aux[:-2]

        for i in range(0, len(acel) - 3):
            acel[i] = acel[i+1] + 1/(aux[i+1] - aux[i])
        acel = acel[:-2]
    
    #print(n)
    return acel

def G_transform(series, error=1e-5):
    n = 4   # initial value
    s = series(n)
    acel = s
    aux1 = np.ones(n + 1, dtype=DT)
    aux2 = np.zeros(n, dtype=DT)

    aux2[0] = s[0]
    for i in range(1, n):
        aux2[i] = s[i] - s[i-1]
    
    while abs(acel[-1] - math.pi**2/6) > error:
        n += 1
        s = series(n)
        acel = s
        aux1 = np.ones(n + 1, dtype=DT)
        aux2 = np.zeros(n, dtype=DT)

        aux2[0] = s[0]
        for i in range(1, n):
            aux2[i] = s[i] - s[i-1]
        
        for i in range(len(aux1) - 2):
            aux1[i] = aux1[i+1] * (aux2[i+1] / aux2[i] - 1)
        aux1 = aux1[:-1]

        for i in range(len(aux2) - 2):
            aux2[i] = aux2[i+1] * (aux1[i+1] / aux1[i] - 1)
        aux2 = aux2[:-1]

        for i in range(len(acel) - 2):
            acel[i] = acel[i] - aux2[i] * (acel[i+1] - acel[i]) / \
                (aux2[i+1] - aux2[i])
        acel = acel[:-1]
            
    #print(n)
    return acel


if __name__ == "__main__":
    
    print("Hello World")
