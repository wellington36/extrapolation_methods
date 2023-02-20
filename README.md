# Acceleration algorithms

This repository contains implementations of the following series transformations:

* [Aitken's transform (or delta-squared process)](https://en.wikipedia.org/wiki/Aitken%27s_delta-squared_process)

## Usage

In `acceleration` we have functions that receive a list of the values of the series to be accelerated along with the number of steps (this being a positive integer or -1 if you want to do the process until you can't do it anymore). Returning the new series in the form of a list. For example:

```python
from acceleration import Aitken_tranform

# a zeta(2) serie
def square_serie(n: int) -> list:
    serie = [0]

    for i in range(1, n):
        serie.append(serie[-1] + 1/(i)**2)
    
    return serie

# create a new serie with the 100 first terms using Aitken acceleration
Aitken_tranform(square_serie(100))
```
