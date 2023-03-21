import math
import numpy as np
from configuration import *

def no_transform(items: np.ndarray, max_steps=10) -> np.ndarray:
    return items

def Aitken_transform(items: np.ndarray, max_steps=10) -> np.ndarray:
    steps = min(int((len(items) - 1) / 2) - 1, max_steps)
    
    for _ in range(steps):
        acel = np.zeros(len(items) - 2, dtype=DT)

        for i in range(0, len(items) - 2):
            acel[i] = (items[i] * items[i+2] - items[i+1]**2) / \
                (items[i+2] - 2 * items[i+1] + items[i])

        items = acel

        if len(acel) < 3:
            return acel
    
    return acel

def Richardson_transform(items: np.ndarray, p=1, max_steps=10) -> np.ndarray:
    """Receive a p that represents the power of the Richardson transform"""
    steps = min(int(math.log2(len(items))) - 2, max_steps)
    
    for _ in range(steps):
        acel = np.zeros(int(len(items)/2), dtype=DT)

        for i in range(0, int(len(items)/2)):
            acel[i] = items[2*i] + (items[2*i] - items[i]) / \
                np.expm1(p * math.log(2))

        items = acel
        p = p + 1
    
    return acel

def Epsilon_transform(items: np.ndarray, max_steps=10) -> np.ndarray:
    # Initial values
    aux = np.zeros(len(items)+1, dtype=DT)
    acel = items
    
    steps = min(int(len(items) / 3) - 2, max_steps)

    for _ in range(steps):
        for i in range(0, len(aux) - 3):
            aux[i] = acel[i+1] + 1/(acel[i+1] - acel[i])
        aux = aux[:-2]

        for i in range(0, len(acel) - 3):
            acel[i] = acel[i+1] + 1/(aux[i+1] - aux[i])
        acel = acel[:-3]
    
    return acel

def G_transform(items: np.ndarray, max_steps=10) -> np.ndarray:
    # Initial values
    aux1 = np.ones(len(items) + 1, dtype=DT)
    aux2 = np.zeros(len(items), dtype=DT)

    aux2[0] = items[0]
    for i in range(1, len(items)):
        aux2[i] = items[i] - items[i-1]
    
    acel = items

    steps = min(int(len(items)/3), max_steps)

    for _ in range(steps):
        for i in range(len(aux1) - 2):
            aux1[i] = aux1[i+1] * (aux2[i+1] / aux2[i] - 1)
        aux1 = aux1[:-1]

        for i in range(len(aux2) - 2):
            aux2[i] = aux2[i+1] * (aux1[i+1] / aux1[i] - 1)
        aux2 = aux2[:-1]

        for i in range(len(acel) - 2):
            acel[i] = acel[i] - aux2[i] * (acel[i+1] - acel[i])/(aux2[i+1] - aux2[i])
        acel = acel[:-3]
    
    return acel


def acceleration(series, transform, error=1e-5, max_steps=5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = transform(series(n0))
    i = -1  # trash

    while abs(acel[-1] - constants[3]) > error: # check error
        i = i + 1
        n = n0 + 2**i
        acel = transform(series(n), max_steps=max_steps)
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = transform(series(int((n+n0)/2)), max_steps=max_steps)

        if abs(acel[-1] - constants[3]) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = transform(series(n), max_steps=max_steps)

    print(n)
    return acel


if __name__ == "__main__":
    
    print("Hello World")
