# Acceleration algorithms

This repository contains implementations of the following series transformations:

* [Aitken's transformation (or delta-squared process)](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process):
  - Per step: O($n$)

* [Richardson's transformation (modify, with given p)](https://en.wikipedia.org/wiki/Richardson_extrapolation):
  - Per step: O($\log n$)

* [Epsilon transformation](https://www.sciencedirect.com/science/article/pii/S0377042700003551):
  - Per step: O($n$)

* [G transformation](https://epubs.siam.org/doi/abs/10.1137/0704032?journalCode=sjnaam):
  - Per step: O($n$)

## Usage

In `acceleration.py` we have functions that receive a list of the values of the series to be accelerated along with the number of steps (this being a positive integer or -1 if you want to do the process until you can't do it anymore). Returning the new series in the form of a list. For example:

```python
from acceleration import Aitken_tranform

# a zeta(2) series
def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, sum of math.pi**2 / 6"""
    series = np.zeros(n, dtype='float64')
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

# create a new series with the 100 first terms using Aitken acceleration
accelerated_series = Aitken_tranform(square_series(100))
```
