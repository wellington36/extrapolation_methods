import math
import numpy as np

# Zeta function test
zeta_2 = lambda x: 1 / x**2
zeta_lower = lambda x: 1 / x**1.0000001


################################


# Richardson extrapolation
def Richardson_aux(f, n, p=1):
    """
    Richardson extrapolation by steps
    f: function
    n: number of points
    """
    s = np.zeros(n)
    s[0] = f(1)

    for i in range(1, n):
        s[i] = f(i+1) + s[i-1]
    
    if n == 1:
        return s[0]
    
    while n > 1:
        r_series = np.zeros(int(n/2))
    
        for i in range(1, int(n/2)+1):
            r_series[i-1] = s[2*i-1] + (s[2*i-1] - s[i-1]) / (2**p - 1)
        
        n = len(r_series)
        s = r_series
        p += 1
    
    return r_series

def Richardson(f, tol=1e-6, p=1):
    values = [Richardson_aux(f, 1, p), Richardson_aux(f, 2, p)]

    k = 1

    while abs(values[k] - values[k-1]) > tol:
        k += 1
        values.append(Richardson_aux(f, 2**k, p)) 
    
    return f"step: {k} | value: {values[k][0]}"



if __name__ == '__main__':
    print(Richardson(zeta_lower, 0.00001, 0.0000001))
    