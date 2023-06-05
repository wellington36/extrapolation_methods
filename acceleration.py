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
    acel = np.zeros(items.shape[0] - 2, dtype=DT)

    for i in range(items.shape[0] - 2):
        acel[i] = np.log(items[i+1] + 1/(1/(items[i+2] - items[i+1]) - 1/(items[i+1] - items[i])), dtype=DT)

    return acel

def G_transform(items: np.ndarray) -> np.ndarray:
    # Initial values
    aux = np.zeros(items.shape[0], dtype=DT)
    acel = np.zeros(items.shape[0] - 3, dtype=DT)

    aux[0] = items[0]
    for i in range(1, items.shape[0]):
        aux[i] = items[i] - items[i-1]        
    

    for i in range(acel.shape[0]):
        t0 = aux[i+3]*aux[i+1] +  aux[i] * aux[i+2] + aux[i+1] * aux[i+2] - aux[i+2]**2 - aux[i+3]*aux[i] - aux[i+1]**2
        t1 = (aux[i+2] * aux[i] - (aux[i+1]) ** 2)  * (aux[i+2] - aux[i+1])/t0

        if t1 <= 0.005:
            acel[i] = np.log(items[i] - (aux[i+1] - aux[i+2])*(aux[i+1]**2 - aux[i+2]*aux[i])*1/t0, dtype=DT)
        else:
            acel[i] = np.log(items[i] - (aux[i+2] - aux[i+1])*aux[i+2]/(aux[i+2] - aux[i+3]), dtype=DT)

    return acel

def acceleration(series, transform, error=1e-5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = transform(series(n0))
    i = -1  # trash

    check = np.array([acel[-1], np.log(constants[1]**2/6)], dtype=DT)
    check = np.exp(np.sort(check), dtype=DT)

    while np.sum(np.array([-1, 1]) @ check, dtype=DT) > error: # check error
        i = i + 1
        n = n0 + 2**i
        acel = transform(series(n))

        check = np.array([acel[-1], np.log(constants[1]**2/6)], dtype=DT)
        check = np.exp(np.sort(check), dtype=DT)
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = transform(series(int((n+n0)/2)))

        check = np.array([acel[-1], np.log(constants[1]**2/6)], dtype=DT)
        check = np.exp(np.sort(check), dtype=DT)

        if np.sum(np.array([-1, 1]) @ check, dtype=DT) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = transform(series(n))

    return n, np.exp(acel, dtype=DT)


if __name__ == "__main__":
    
    print("Hello World")
