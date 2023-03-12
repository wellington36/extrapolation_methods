# Acceleration algorithms

This repository contains implementations of the following series transformations:

* [Aitken's transformation (or delta-squared process)](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process):
  - Transform: O($n$)
  - To find n: O($2n\log n$)

* [Richardson's transformation (modify, with given p)](https://en.wikipedia.org/wiki/Richardson_extrapolation):
  - Transform: O($\log n$)
  - To find n: O($2(\log n)^2$)

* [Epsilon transformation](https://www.sciencedirect.com/science/article/pii/S0377042700003551):
  - Transform: O($n$)
  - To find n: O($2n\log n$)

* [G transformation](https://epubs.siam.org/doi/abs/10.1137/0704032?journalCode=sjnaam):
  - Transform: O($n$)
  - To find n: O($2n\log n$)

## Usage

In `acceleration.py` we have the transformations implemented above, and for use we have the `acceleration` function that receives a series (in the form of a function $s: \mathbb{N} \to \mathbb{R}^n$ returning the first n elements of that series), the chosen transformation ("Aitken_tranform", "Richardson_transform", "Epsilon_transform", "G_transform" e "no_transform", the latter being using the initial series without any transformation), the stopping criterion (in case the difference of the last two values of the series are smaller than a given error) and the maximum number of steps the transformation can take. This function finds the smallest n at which, with the transformation, the series error is less than the given error. For example:

```python
from acceleration import *

# a zeta(2) series
def square_series(n: int) -> np.ndarray:
    """Zeta(2) series, sum of math.pi**2 / 6"""
    series = np.zeros(n, dtype='float64')
    series[0] = 1.0

    for i in range(1, n):
        series[i] =  series[i-1] + 1/(i+1)**2
    
    return series

# Creates a new accelerated series with fewer terms than the original and 
# such that the difference of the last two terms is less than the error=1e-5:
accelerated_series = acceleration(square_series, Aitken_tranform, error=1e-5, max_steps=2)
```
