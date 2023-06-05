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

- *A series*: In the form of a function $f: \mathbb{N} \to \mathbb{R}$ returning the terms to be summed.
- *The Transformation*: "Aitken_tranform", "Richardson_transform", "Epsilon_transform", "G_transform" and "no_transform", the latter being using the initial series without any transformation.
- *The stopping criterion*: In case the difference of the last two values of the series are smaller than a given error.

This function determines the minimum value of n for which, when applying the transformation, the difference between the last partial sums becomes smaller than the specified error. For example:


```python
from acceleration import *
import math

# Test with no_transform (without transformation) and with Richardson transformation the basel problem
n0, no_accelerated = acceleration(lambda x: 1/x**2, no_transform, error=1e-12)
n1, accelerated = acceleration(lambda x: 1/x**2, Richardson_transform, error=1e-12)

# Comparison
print(f"True value:           {math.pi ** 2 / 6}")
print(f"Without acceleration: {no_accelerated[-1]}, with {n0} iterations")
print(f"With acceleration:    {accelerated[-1]}, with {n1} iterations")
```

Out:
```
True value:           1.6449340668482264
Without acceleration: 1.6449330668487265, with 1000000 iterations
With acceleration:    1.644934061125596, with 22896 iterations
```
