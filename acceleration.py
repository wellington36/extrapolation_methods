import math
import numpy as np

# SET DATA TYPE
DT = np.dtype('float64') # float 64 bits


def Aitken_tranform(items: np.ndarray, steps=-1) -> np.ndarray:
    if steps == -1:
        steps = int((len(items) - 1) / 2)
    
    for _ in range(steps):
        acel = np.zeros(len(items) - 2, dtype=DT)

        for i in range(0, len(items) - 2):
            acel[i] = (items[i] * items[i+2] - items[i+1]**2) / \
                (items[i+2] - 2 * items[i+1] + items[i])

        items = acel

        if len(acel) < 3:
            return acel
        
    return acel

def Richardson_transform(items: np.ndarray, p=1, steps=-1) -> np.ndarray:
    """Receive a p that represents the power of the Richardson transform"""
    if steps == -1:
        steps = int(math.log2(len(items))) - 1
    
    for _ in range(steps):
        acel = np.zeros(int(len(items)/2), dtype=DT)

        for i in range(0, int(len(items)/2)):
            acel[i] = items[2*i] + (items[2*i] - items[i]) / (2**p - 1)

        items = acel
        p = p + 1
    
    return acel

#def Richardson_transform(items: list, p=1, steps=-1) -> list:
#    """Receive a p that represents the power of the Richardson transform"""
#    if steps == -1:
#        steps = int(math.log2(len(items))) - 1
#    
#    for _ in range(steps):
#        acel = []
#
#        for i in range(0, int(len(items)/2)):
#            acel.append(items[2*i] + (items[2*i] - items[i]) / (2**p - 1))
#
#        items = acel
#        p = p + 1
#    
#    return acel

def Epsilon_transfom(items: list, steps=-1) -> list:
    # Initial values
    aux = [0 for _ in range(len(items)+1)]
    acel = items

    if steps == -1:
        steps = int(len(items) / 2) - 1

    for _ in range(steps):
        for i in range(0, len(aux) - 3):
            aux[i] = acel[i+1] + 1/(acel[i+1] - acel[i])
        aux = aux[:-2]

        for i in range(0, len(acel) - 3):
            acel[i] = acel[i+1] + 1/(aux[i+1] - aux[i])
        acel = acel[:-2]
        
    
    return acel


def G_transform(items: list, steps=-1) -> list:
    # Initial values
    aux1 = [1 for _ in range(len(items))]
    aux2 = [items[0]] + [items[i+1] - items[i]  for i in range(len(items)-1)]
    acel = items

    if steps == -1:
        steps = len(items) - 1

    for _ in range(steps):
        for i in range(len(aux1) - 2):
            aux1[i] = aux1[i+1] * (aux2[i+1] / aux2[i] - 1)
        aux1 = aux1[:-1]

        for i in range(len(aux2) - 2):
            aux2[i] = aux2[i+1] * (aux1[i+1] / aux1[i] - 1)
        aux2 = aux2[:-1]


        print(f"{len(aux1)},  {len(aux2)}, {len(acel)}")
        for i in range(len(acel) - 2):
            acel[i] = acel[i] - aux2[i] * (acel[i+1] - acel[i])/(aux2[i+1] - aux2[i])
        acel = acel[:-1]

    return acel


if __name__ == "__main__":
    
    print("Hello World")
