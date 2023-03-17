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

In `acceleration.py` we have the transformations implemented above, and for use have the `acceleration` function, that receives on input:

- *A series*: In the form of a function $s: \mathbb{N} \to \mathbb{R}^n$ returning the first n elements of that series.
- *The Transformation*: "Aitken_tranform", "Richardson_transform", "Epsilon_transform", "G_transform" and "no_transform", the latter being using the initial series without any transformation.
- *The stopping criterion*: In case the difference of the last two values of the series are smaller than a given error.
- *The maximum number of steps*: In general, transformations can be applied multiple times on the same series.

This function find the smallest n at which, with the transformation, the series error is less than the given error. For example:


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

# Test with no_transform (without transformation) and with Richardson transformation
no_accelerated = acceleration(square_series, no_transform, error=1e-5, max_steps=2)
accelerated = acceleration(square_series, Richardson_transform, error=1e-5, max_steps=2)

# Comparison
print(f"True value:           {math.pi ** 2 / 6}")
print(f"Without acceleration: {no_accelerated[-1]}")
print(f"With acceleration:    {accelerated[-1]}")
```

Out:
```
True value:           1.6449340668482264
Without acceleration: 1.6417844631526846
With acceleration:    1.6448860927420919
```
