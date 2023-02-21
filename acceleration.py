import math

def Aitken_tranform(items: list, steps=-1) -> list:
    if steps == -1:
        steps = int((len(items) - 1) / 2)

    for _ in range(steps):
        acel = []

        for i in range(0, len(items) - 2):
            acel.append((items[i] * items[i+2] - items[i+1]**2) / \
                (items[i+2] - 2* items[i+1] + items[i]))

        items = acel

        if len(acel) < 3:
            return acel
    
    return acel

def Richardson_transform(items: list, p=1, steps=-1) -> list:
    """Receive a p that represents the power of the Richardson transform"""
    if steps == -1:
        steps = int(math.log2(len(items))) - 1
    
    for _ in range(steps):
        acel = []

        for i in range(0, int(len(items)/2)):
            acel.append(items[2*i] + (items[2*i] - items[i]) / (2**p - 1))

        items = acel
        p = p + 1
    
    return acel

def Epsilon_transfom(items: list, steps=-1) -> list:
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
    pass



if __name__ == "__main__":
    
    print("Hello")
