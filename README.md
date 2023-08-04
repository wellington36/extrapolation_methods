Acceleration algorithms
==================

Let be $S_n = \sum_{i=1}^n a_i$ a sequence of parcial sums. This repository contains implementations of the following series transformations, which generate a new sequence $T_n$:

* [Aitken's transformation (or delta-squared process)](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process):
  - In `esum`: O($2n\log n$)
  - In `acelsum`: O($n$)

  $$T_n = \frac{S_{n-1} S_{n+1} - S_n^2}{S_{n+1} - 2 S_n + S_{n-1}}.$$

* [Richardson's transformation (modify, with given p)](https://en.wikipedia.org/wiki/Richardson_extrapolation):
  - In `esum`: O($2(\log n)^2$)
  - In `acelsum`: O($\log n$)

  $$T_n = S_{2n} + \frac{S_{2n} - S_n}{2^p - 1}.$$

  Here, we use $p = 1$ for simplicity.

* [Epsilon transformation](https://www.sciencedirect.com/science/article/pii/S0377042700003551):
  - In `esum`: O($2n\log n$)
  - In `acelsum`: O($n$)

  Let be the auxiliary sequence $\varepsilon_n^j$ defined by:

  $$\varepsilon_{-1}^{j} = 0\ \text{and}\ \varepsilon_{0}^{j} = S_j,$$

  and inductively:

  $$\varepsilon_{k+1}^{j} = \varepsilon_{k-1}^{j+1} + [\varepsilon_{k}^{j+1} - \varepsilon_{k}^{j}]^{-1}.$$

  Then, $T_n = \varepsilon_{n-1}^{2}$ (because the odd steps are only partial steps).


* [G transformation](https://www.cambridge.org/core/books/abs/practical-extrapolation-methods/gtransformation-and-its-generalizations/B3A1C6628B6C3E6438C943E25FFA621D):
  - In `esum`: O($4n\log n$)
  - In `acelsum`: O($2n$)

  Let be two auxiliary sequences $s_j^{(n)}$ and $r_j^{(n)}$ defined by:

  $$s^{(n)}_0 = 1,\ r^{(n)}_1 = x_n,\ n=0,1,\ldots,$$

  inductively:

  $$s^{(n)}_{k+1} = s^{(n+1)}_{k} ( \frac{r^{(n+1)}_{k+1}}{r^{(n)}_{k+1}} - 1),\ k,n = 0,1,\ldots$$
  
  and


  $$r^{(n)}_{k+1} = r^{(n+1)}_{k} \left( \frac{s^{(n+1)}_{k}}{s^{(n)}_{k}} - 1 \right),\ k=1,2,\ldots;\ n=0,1,\ldots$$

  Then, $T_n = S_n - \frac{S_{n+1} - S_{n}}{r^{(n+1)}_{1} - r^{(n)}_{1}} r^{(n)}_{1}$.

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
from extrapolation import esum
import math

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
from extrapolation import acelsum
import math

# Test with no_transform (without transformation) and with Richardson transformation the basel problem
no_accelerated = acelsum(lambda x: 1/x**2, 'None', n=1000, logarithm=False, precision=100)
accelerated = acelsum(lambda x: 1/x**2, 'Richardson', n=1000, logarithm=False, precision=100)

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
