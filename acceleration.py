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

def Richardson_transform(items, p=1, steps=-1) -> list:
    if steps == -1:
        steps = int(math.log2(len(items))) - 1
    
    for _ in range(steps):
        acel = []

        for i in range(0, int(len(items)/2)):
            acel.append(items[2*i] + (items[2*i] - items[i]) / (2**p - 1))

        items = acel
        p = p + 1
    
    return acel

if __name__ == "__main__":
    
    print("Hello")
