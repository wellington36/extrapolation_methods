Acceleration algorithms
==================

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

## Installation

To install the package, run the following command:

```bash
pip install extrapolation
```

## Usage

We have the transformations implemented above, and for use have the `esum` and `acelsum` function.

### esum
The `esum` receives on input:

- *A series*: In the form of a function $f: \mathbb{N} \to \mathbb{R}$ returning the terms to be summed.
- *The Transformation*: "Aitken", "Richardson", "Epsilon", "G" and "None", the latter being using the initial series without any transformation.
- *The stopping criterion*: In case the difference of the last two values of the series are smaller than a given error.
- *Return in logarithm scale*: True if you want to receive the return in logarithm scale with the sign and False if you want to receive in normal scale.
- *Precision*: If precision is 53 we use the default python precision, otherwise the given bits precision.

This function determines the minimum value of n for which, the difference between the last partial sums becomes less than the specified error when applying the transformation. And returns the series applied to the transformation. The following is an example:


```python
from acceleration.esum import *

# Test with no_transform (without transformation) and with Richardson transformation the basel problem
n0, no_accelerated = esum(lambda x: 1/x**2, 'None', error=1e-12, logarithm=False, precision=100)
n1, accelerated = esum(lambda x: 1/x**2, 'Richardson', error=1e-12, logarithm=False, precision=100)

# Comparison
print(f"True value:           {math.pi ** 2 / 6}")
print(f"Without acceleration: {no_accelerated[-1]}, with {n0} iterations")
print(f"With acceleration:    {accelerated[-1]}, with {n1} iterations")
```

Out:
```
True value:           1.6449340668482264
Without acceleration: 1.6449330668607708753650232828, with 1000012 iterations
With acceleration:    1.6449340611256049164589309217, with 22896 iterations
```

### acelsum
We have also the `acelsum` function, that receives on input:

- *A series*: In the form of a function $f: \mathbb{N} \to \mathbb{R}$ returning the terms to be summed.
- *The Transformation*: "Aitken", "Richardson", "Epsilon", "G" and "None", the latter being using the initial series without any transformation.
- *Natural n*: Number of values to be summed.
- *Return in logarithm scale*: True if you want to receive the return in logarithm scale with the sign and False if you want to receive in normal scale.
- *Precision*: If precision is 53 we use the default python precision, otherwise the given bits precision.

This function calculates partial sums up to a given natural value, returning the result in log-scale or normal by applying a chosen transformation. The following is an example:

```python
from acceleration.esum import *

# Test with no_transform (without transformation) and with Richardson transformation the basel problem
no_accelerated = acelsum(lambda x: 1/x**2, 'None', n=1000, logarithm=False, precision=100)
accelerated = esum(lambda x: 1/x**2, 'Richardson', n=1000, logarithm=False, precision=100)

# Comparison
print(f"True value:           {math.pi ** 2 / 6}")
print(f"Without acceleration: {no_accelerated[-1]}")
print(f"With acceleration:    {accelerated[-1]}")
```

Out:
```
True value:           1.6449340668482264
Without acceleration: 1.6439345666815597935850701245
With acceleration:    1.6449310678482254269248263997
```
