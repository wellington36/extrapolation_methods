from mpmath import mp, mpf, nsum, log, expm1, fabs, pi, exp
import matplotlib.pyplot as plt
import numpy as np
import time

###### CONSTANTS ######
mp.prec = 500
np_type = mpf

###### TEST SERIES ######
def basel_problem(n):
    return 1/n**2

def slow_convergence_series(n):
    return 1/(n * (np.log(n))**2)


###### TRANSFORMS ######
def richardson(item: np.ndarray, p: int = 1):
    """Richardson extrapolation on a numpy array"""
    acel = np.zeros(int(item.shape[0]/2), dtype=np_type)

    for i in range(int(item.shape[0]/2)):
        acel[i] = item[2*i] + (item[2*i] - item[i]) / \
            expm1(p * log(mpf('2')))
        
        acel[i] = log(acel[i])
    
    return acel


###### PARTIAN SUMS ######
def partial_sum_mpmath(f, n):
    """Return the partial sum of a series"""
    series = np.zeros(n, dtype=np_type)
    series[0] = mpf(f(1))

    for i in range(1, n):
        series[i] = series[i-1] + mpf(f(i+1))
    
    return series

###### ACCELERATION ######
def acceleration(series, error=1e-5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = richardson(partial_sum_mpmath(series, n))
    i = -1  # trash

    while (fabs(exp(acel[-1]) - pi**2/6)  > error): # check error
        i = i + 1
        n = n0 + 2**i
        acel = richardson(partial_sum_mpmath(series, n))
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = richardson(partial_sum_mpmath(series, int((n+n0)/2)))

        if (fabs(exp(acel[-1]) - pi**2/6)  > error):    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = richardson(partial_sum_mpmath(series, n))

    return n, np.vectorize(exp)(acel)

###### MAIN ######
if __name__ == "__main__":
    e = 1e-6

    for t in [acceleration]:
        
        if t in []:
            continue

        print(f"########## {e} ##########")
        t0 = time.time()
        n, acel = t(basel_problem, error=e)
        t1 = time.time() - t0

        t0 = time.time()
        n, acel = t(basel_problem, error=e)
        t2 = time.time() - t0

        t0 = time.time()
        n, acel = t(basel_problem, error=e)
        t3 = time.time() - t0

        print(f"{t.__name__}    |   {(t1 + t2 + t3) / 3} |   {acel[-1]}  |   {n}")

        plt.plot(range(len(acel)), acel, label=t.__name__)
    
    plt.legend()
    plt.show()