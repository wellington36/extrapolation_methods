from mpmath import mp, mpf, exp, log, expm1, pi, fabs
#import matplotlib.pyplot as plt
import numpy as np
import time

###### CONSTANTS ######
mp.dps = 17
np_prec = np.dtype('float64') 

###### TEST SERIES ######
def basel_problem(n):
    return 1/n**2

def slow_convergence_series(n):
    return 1/(n * (np.log(n))**2)


###### TRANSFORMS ######
def richardson_numpy(item: np.ndarray, p: int = 1):
    """Richardson extrapolation on a numpy array"""
    acel = np.zeros(int(item.shape[0]/2), dtype=np_prec)

    for i in range(int(item.shape[0]/2)):
        acel[i] = item[2*i] + (item[2*i] - item[i]) / \
            np.expm1(p * np.log(2, dtype=np_prec), dtype=np_prec)
        
        acel[i] = np.log(acel[i], dtype=np_prec)
    
    return acel

def richardson_mpmath(item: list, p: int = 1):
    """Richardson extrapolation on a mpmath array"""
    acel = []

    for i in range(int(len(item)/2)):
        acel.append(log(item[2*i] + (item[2*i] - item[i]) / expm1(p * log(2))))
        
    return acel


###### PARTIAN SUMS ######
def partial_sum_numpy(f, n):
    """Return the partial sum of a series"""
    series = np.zeros(n, dtype=np_prec)
    series[0] = f(1)

    for i in range(1, n):
        series[i] = series[i-1] + f(i+1)
    
    return series

def partial_sum_mpmath(f, n):
    """Return the partial sum of a series"""
    series = [mpf(f(1))]

    for i in range(1, n):
        series.append(series[i-1] + mpf(f(i+1)))
    
    return series


###### ACCELERATION ######
def acceleration_numpy(series, error=1e-5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = richardson_numpy(partial_sum_numpy(series, n))
    i = -1  # trash

    check = np.array([acel[-1], np.log(np.pi**2/6, dtype=np_prec)], dtype=np_prec)
    check = np.exp(np.sort(check), dtype=np_prec)

    while np.sum(np.array([-1, 1]) @ check, dtype=np_prec) > error: # check error
        i = i + 1
        n = n0 + 2**i
        acel = richardson_numpy(partial_sum_numpy(series, n))

        check = np.array([acel[-1], np.log(np.pi**2/6, dtype=np_prec)], dtype=np_prec)
        check = np.exp(np.sort(check), dtype=np_prec)
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = richardson_numpy(partial_sum_numpy(series, int((n+n0)/2)))

        check = np.array([acel[-1], np.log(np.pi**2/6, dtype=np_prec)], dtype=np_prec)
        check = np.exp(np.sort(check), dtype=np_prec)

        if np.sum(np.array([-1, 1]) @ check, dtype=np_prec) > error:    # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = richardson_numpy(partial_sum_numpy(series, n))

    return n, np.exp(acel, dtype=np_prec)

def acceleration_mpmath(series, error=1e-5) -> np.ndarray:
    n0 = 10
    n = n0
    acel = richardson_mpmath(partial_sum_mpmath(series, n))
    i = -1  # trash

    while (fabs(exp(acel[-1]) - pi**2/6) > error): # check error
        i = i + 1
        n = n0 + 2**i
        acel = richardson_mpmath(partial_sum_mpmath(series, n))
    
    n0 = n0 + 2**(i-1)

    while (n > n0):
        acel = richardson_mpmath(partial_sum_mpmath(series, int((n+n0)/2)))

        if (fabs(exp(acel[-1]) - pi**2/6) > error): # check error
            n0 = int((n+n0)/2 + 1)
        else:
            n = int((n+n0)/2)
        
    acel = richardson_mpmath(partial_sum_mpmath(series, n))

    return n, [exp(i) for i in acel]

###### MAIN ######
if __name__ == "__main__":
    e = 1e-8

    for t in [acceleration_numpy, acceleration_mpmath]:
        
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

        #plt.plot(range(len(acel)), acel, label=t.__name__)
    
    #plt.legend()
    #plt.show()