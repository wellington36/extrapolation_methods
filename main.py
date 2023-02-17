import math

def Aitken_tranform(items: list, steps=-1) -> list:
    if steps == -1:
        steps = int((len(items) - 1) / 2)

    for _ in range(steps):
        acel = []

        for i in range(0, len(items) - 2):
            acel.append((items[i] * items[i+2] - items[i+1]**2) / \
                (items[i+2] - 2* items[i+1] + items[i]))

        #print(acel) # checking

        items = acel

        if len(acel) < 3:
            return acel[-1]
    
    return acel[0]


if __name__ == "__main__":
    # serie = [1/1, 5/4, 49/36, 205/144, 5269/3600, 5369/3600, 266681/176400]
    print(Aitken_tranform([1/1, 5/4, 49/36, 205/144, 5269/3600, 5369/3600, 266681/176400]))