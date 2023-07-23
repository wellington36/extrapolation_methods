from mpmath import mp, mpf, exp, log, expm1, pi, fabs
from acceleration.configuration import *
from acceleration.utils import *


###### partial sum ######
def partial_sum_mp(f, n: int) -> list:
    """Return the partial sum of the series f, up to n terms"""
    series = [None] * n

    series[0] = mpf(f(1))

    for i in range(1, n):
        series[i] = series[i-1] + mpf(f(i+1))
    
    return [create_lognumber(i) for i in series]


###### extrapolation methods ######
def no_transform_mp(items: list) -> list:
    return items

def Aitken_transform_mp(items: list) -> list:
    acel = [None] * (len(items) - 2)

    for i in range(len(items) - 2):
        t0 = items[i] + (items[i+2] - items[i+1] * 2)

        acel[i] = items[i+2] * (items[i])/t0 - items[i+1] * (items[i+1])/t0
    
    return acel


###### summation with extrapolation ######
def emsum(series, transform, error=1e-5):
    n0 = 10
    n = n0
    acel = transform(partial_sum_mp(series, n0))
    i = -1  # trash

    while fabs(exp(acel[-1].return_value()[1]) - exp(acel[-2].return_value()[1])) > error:
        i = i + 1
        n = n0 + 2**i
        acel = transform(partial_sum_mp(series, n))
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = transform(partial_sum_mp(series, int((n+n0)/2)))

        if fabs(exp(acel[-1].return_value()[1]) - exp(acel[-2].return_value()[1])) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = transform(partial_sum_mp(series, n))

    return n, [i.return_value() for i in acel]


if __name__ == "__main__":
    
    print("Hello World")
    