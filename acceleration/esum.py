from mpmath import mp, mpf, exp, log, expm1, fabs
from acceleration.utils import *


###### partial sum ######
def partial_sum_mp(f, n: int) -> list:
    """Return the partial sum of the series f, up to n terms"""
    series = [None] * n

    series[0] = mpf(f(1))

    for i in range(1, n):
        series[i] = series[i-1] + mpf(f(i+1))
    
    return [create_lognumber(i, lib='mpmath') for i in series]


def partial_sum_list(f, n: int) -> list:
    """Return the partial sum of the series f, up to n terms"""
    series = [None] * n
    series[0] = f(1)

    for i in range(1, n):
        series[i] = series[i-1] + f(i+1)
    
    return [create_lognumber(i, lib='math') for i in series]


###### extrapolation methods ######
def no_transform(items: list, lib='mpmath') -> list:
    return items

def Aitken_transform(items: list, lib='mpmath') -> list:
    acel = [None] * (len(items) - 2)

    for i in range(len(items) - 2):
        t0 = items[i] + (items[i+2] - items[i+1] * 2)

        acel[i] = items[i+2] * (items[i])/t0 - items[i+1] * (items[i+1])/t0
    
    return acel

def Richardson_transform(item: list, p: int = 1, lib='mpmath') -> list:
    """Receive a p that represents the power of the Richardson transform"""
    acel = [None] * int(len(item)/2)

    for i in range(int(len(item)/2)):
        if lib == 'mpmath':
            acel[i] = item[2*i] + (item[2*i] - item[i]) / expm1(p * log(2))
        else:
            acel[i] = item[2*i] + (item[2*i] - item[i]) / (2**p - 1)
    
    return acel

def Epsilon_transform(items: list, lib='mpmath') -> list:
    acel = [None] * (len(items) - 2)

    for i in range(len(items) - 2):
        acel[i] = items[i+1] + ((items[i+2] - items[i+1])**(-1) - (items[i+1] - items[i])**(-1))**(-1)

    return acel

def G_transform(items: list, lib='mpmath') -> list:
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
            acel[i] = items[i] - (aux[i+1] - aux[i+2])*(aux[i+1]**2 - aux[i+2]*aux[i])*1/t0
        else:
            acel[i] = items[i] - (aux[i+2] - aux[i+1])*aux[i+2]/(aux[i+2] - aux[i+3])

    return acel


###### summation with extrapolation ######
def acelsum(series, transform, n, precision=53):
    transformation = {'Aitken': Aitken_transform,
                      'Richardson': Richardson_transform,
                      'Epsilon': Epsilon_transform,
                      'G': G_transform,
                      'None': no_transform}

    transform = transformation[transform]

    if precision == 53:
        acel = transform(partial_sum_list(series, n), lib='math')
    else:
        mp.prec = precision
        acel = transform(partial_sum_mp(series, n), lib='mpmath')

    return acel

def esum(series, transform, error=1e-5, logarithm=False, precision=53):
    n0 = 10
    n = n0
    acel = acelsum(series, transform, n0, precision)
    i = -1  # trash

    while fabs(exp(acel[-1].value()[1]) - exp(acel[-2].value()[1])) > error:
        i = i + 1
        n = n0 + 2**i
        acel = acelsum(series, transform, n)
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = acelsum(series, transform, int((n+n0)/2))

        if fabs(exp(acel[-1].value()[1]) - exp(acel[-2].value()[1])) > error:
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = acelsum(series, transform, n)

    if logarithm:
        return n, acel
    
    return n, [i.exp(precision) for i in acel]


if __name__ == '__main__':
    print("This is a module.  Do not run it directly.")
    exit(1)
    