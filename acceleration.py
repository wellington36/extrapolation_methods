import math
import numpy as np
from configuration import *

def no_transform(items: np.ndarray) -> np.ndarray:
    return np.log(items, dtype=DT)

def Aitken_transform(items: np.ndarray) -> np.ndarray:
    acel = np.zeros(items.shape[0] - 2, dtype=DT)

    for i in range(items.shape[0] - 2):
        t0 = items[i] + (items[i+2] - 2 * items[i+1])

        acel[i] = np.log(items[i+2] * (items[i])/t0 - items[i+1] * (items[i+1])/t0, dtype=DT)
    
    return acel

def Richardson_transform(item: np.ndarray, p: int = 1) -> np.ndarray:
    """Receive a p that represents the power of the Richardson transform"""
    acel = np.zeros(int(item.shape[0]/2), dtype=DT)

    for i in range(int(item.shape[0]/2)):
        acel[i] = item[2*i] + (item[2*i] - item[i]) / \
            np.expm1(p * math.log(2), dtype=DT)
        
        acel[i] = np.log(acel[i], dtype=DT)
    
    return acel

def Epsilon_transform(items: np.ndarray) -> np.ndarray:
    # Initial values
    aux = np.zeros(items.shape[0]+1, dtype=DT)
    acel = items

    for i in range(0, aux.shape[0] - 3):
        aux[i] = acel[i+1] + 1/(acel[i+1] - acel[i])
    aux = aux[:-3]

    for i in range(0, acel.shape[0] - 3):
        acel[i] = np.log(acel[i+1] + 1/(aux[i+1] - aux[i]), dtype=DT)
    acel = acel[:-3]
    
    return acel

def G_transform(items: np.ndarray) -> np.ndarray:
    # Initial values
    aux1 = np.ones(items.shape[0] + 1, dtype=DT)
    aux2 = np.zeros(items.shape[0], dtype=DT)

    aux2[0] = items[0]
    for i in range(1, items.shape[0]):
        aux2[i] = items[i] - items[i-1]
        
    acel = items

    for i in range(aux1.shape[0] - 2):
        aux1[i] = aux1[i+1] * (aux2[i+1] / aux2[i] - 1)
    aux1 = aux1[:-1]

    for i in range(aux2.shape[0] - 2):
        aux2[i] = aux2[i+1] * (aux1[i+1] / aux1[i] - 1)
    aux2 = aux2[:-1]

    for i in range(acel.shape[0] - 2):
        acel[i] = np.log(acel[i] - aux2[i] * (acel[i+1] - acel[i])/(aux2[i+1] - aux2[i]), dtype=DT)
    acel = acel[:-3]

    return acel


def acceleration(series, transform, error=1e-5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = transform(series(n0))
    i = -1  # trash

    check = np.array([acel[-1], acel[-2]], dtype=DT)
    check = np.exp(np.sort(check), dtype=DT)

    while np.sum(np.array([-1, 1]) @ check, dtype=DT) > error: # check error
        i = i + 1
        n = n0 + 2**i
        acel = transform(series(n))

        check = np.array([acel[-1], acel[-2]], dtype=DT)
        check = np.exp(np.sort(check), dtype=DT)
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = transform(series(int((n+n0)/2)))

        check = np.array([acel[-1], acel[-2]], dtype=DT)
        check = np.exp(np.sort(check), dtype=DT)

        if np.sum(np.array([-1, 1]) @ check, dtype=DT) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = transform(series(n))

    return n, np.exp(acel, dtype=DT)


if __name__ == "__main__":
    
    print("Hello World")
