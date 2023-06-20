from mpmath import mp, mpf, exp, log, expm1, pi, fabs
from acceleration.configuration import *


###### partial sum ######
def partial_sum_mp(f, n: int) -> list:
    """Return the partial sum of the series f, up to n terms"""
    series = [None] * n

    series[0] = mpf(f(1))

    for i in range(1, n):
        series[i] = series[i-1] + mpf(f(i+1))
    
    return series


###### extrapolation methods ######
def no_transform_mp(items: list) -> list:
    return [log(item) for item in items]

def Aitken_transform_mp(items: list) -> list:
    acel = [None] * (len(items) - 2)

    for i in range(len(items) - 2):
        t0 = items[i] + (items[i+2] - 2 * items[i+1])

        acel[i] = log(items[i+2] * (items[i])/t0 - items[i+1] * (items[i+1])/t0)
    
    return acel

def Richardson_transform_mp(item: list, p: int = 1) -> list:
    """Receive a p that represents the power of the Richardson transform"""
    acel = [None] * int(len(item)/2)

    for i in range(int(len(item)/2)):
        acel[i] = item[2*i] + (item[2*i] - item[i]) / \
            expm1(p * log(2))
        
        acel[i] = log(acel[i])
    
    return acel

def Epsilon_transform(items: np.ndarray) -> np.ndarray:
    acel = np.zeros(items.shape[0] - 2, dtype=DT)

    for i in range(items.shape[0] - 2):
        acel[i] = np.log(items[i+1] + 1/(1/(items[i+2] - items[i+1]) - 1/(items[i+1] - items[i])), dtype=DT)

    return acel

def Epsilon_transform_mp(items: list) -> list:
    acel = [None] * (len(items) - 2)

    for i in range(len(items) - 2):
        acel[i] = log(items[i+1] + 1/(1/(items[i+2] - items[i+1]) - 1/(items[i+1] - items[i])))

    return acel

def G_transform_mp(items: list) -> list:
    # Initial values
    aux = [None] * len(items)
    acel = [None] * (len(items) - 3)

    aux[0] = items[0]
    for i in range(1, len(items)):
        aux[i] = items[i] - items[i-1]        
    

    for i in range(len(acel)):
        t0 = aux[i+3]*aux[i+1] +  aux[i] * aux[i+2] + aux[i+1] * aux[i+2] - aux[i+2]**2 - aux[i+3]*aux[i] - aux[i+1]**2
        t1 = (aux[i+2] * aux[i] - (aux[i+1]) ** 2)  * (aux[i+2] - aux[i+1])/t0

        if t1 <= 0.005:
            acel[i] = log(items[i] - (aux[i+1] - aux[i+2])*(aux[i+1]**2 - aux[i+2]*aux[i])*1/t0)
        else:
            acel[i] = log(items[i] - (aux[i+2] - aux[i+1])*aux[i+2]/(aux[i+2] - aux[i+3]))

    return acel


###### summation with extrapolation ######
def emsum(series, transform, error=1e-5):
    n0 = 10
    n = n0
    acel = transform(partial_sum_mp(series, n0))
    i = -1  # trash

    while fabs(exp(acel[-1]) - exp(acel[-2])) > error:
        i = i + 1
        n = n0 + 2**i
        acel = transform(partial_sum_mp(series, n))
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = transform(partial_sum_mp(series, int((n+n0)/2)))

        if fabs(exp(acel[-1]) - exp(acel[-2])) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = transform(partial_sum_mp(series, n))

    return n, [exp(i) for i in acel]


if __name__ == "__main__":
    
    print("Hello World")
    