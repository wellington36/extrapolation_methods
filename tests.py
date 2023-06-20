from acceleration.esum import esum, no_transform, Richardson_transform, Aitken_transform, Epsilon_transform, G_transform, partial_sum
import numpy as np

def basel_series(n: int):
    return 1/(n)**2

def equivalence(a, b, epsilon=0.0001):
    return abs(a - b) < epsilon

#################### TESTS ####################

def test_partial_sum():
    array = partial_sum(basel_series, 4)

    assert type(array) == np.ndarray
    assert len(array) == 4
    assert equivalence(array[0], 1)
    assert equivalence(array[1], 5/4)
    assert equivalence(array[2], 49/36)
    assert equivalence(array[3], 205/144)

def test_len_transformations():
    assert len(no_transform(partial_sum(basel_series, 10))) == 10
    assert len(Aitken_transform(partial_sum(basel_series, 10))) == 8
    assert len(Richardson_transform(partial_sum(basel_series, 10))) == 5
    assert len(Epsilon_transform(partial_sum(basel_series, 10))) == 8
    assert len(G_transform(partial_sum(basel_series, 10))) == 7

def test_simple_acceleration():
    n, acel = esum(basel_series, no_transform, 0.1)
    assert type(n) == int
    assert type(acel) == np.ndarray
    assert len(acel) == 10

    n, acel = esum(basel_series, no_transform, 0.01)
    assert type(n) == int
    assert type(acel) == np.ndarray
    assert len(acel) == 100


if __name__ == '__main__':
    test_partial_sum()
    test_len_transformations()
    test_simple_acceleration()