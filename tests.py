from acceleration.esum import esum, no_transform_np, Richardson_transform_np, Aitken_transform_np, Epsilon_transform_np, G_transform_np, partial_sum_np
from acceleration.emsum import emsum, no_transform_mp, Richardson_transform_mp, Aitken_transform_mp, Epsilon_transform_mp, G_transform_mp, partial_sum_mp
import numpy as np

def basel_series(n: int):
    return 1/(n)**2

def equivalence(a, b, epsilon=0.0001):
    return abs(a - b) < epsilon

#################### TESTS numpy ####################

def test_partial_sum_np():
    array = partial_sum_np(basel_series, 4)

    assert type(array) == np.ndarray
    assert len(array) == 4
    assert equivalence(array[0], 1)
    assert equivalence(array[1], 5/4)
    assert equivalence(array[2], 49/36)
    assert equivalence(array[3], 205/144)

def test_len_transformations_np():
    assert len(no_transform_np(partial_sum_np(basel_series, 10))) == 10
    assert len(Aitken_transform_np(partial_sum_np(basel_series, 10))) == 8
    assert len(Richardson_transform_np(partial_sum_np(basel_series, 10))) == 5
    assert len(Epsilon_transform_np(partial_sum_np(basel_series, 10))) == 8
    assert len(G_transform_np(partial_sum_np(basel_series, 10))) == 7

def test_simple_acceleration_np():
    n, acel = esum(basel_series, no_transform_np, error=0.1)
    assert type(n) == int
    assert type(acel) == np.ndarray
    assert len(acel) == n

    n, acel = esum(basel_series, no_transform_np, error=0.01)
    assert type(n) == int
    assert type(acel) == np.ndarray
    assert len(acel) == n

#################### TESTS mpmath ####################
def test_partial_sum_mp():
    array = partial_sum_mp(basel_series, 4)

    assert type(array) == list
    assert len(array) == 4
    assert equivalence(array[0], 1)
    assert equivalence(array[1], 5/4)
    assert equivalence(array[2], 49/36)
    assert equivalence(array[3], 205/144)


def test_len_transformations_mp():
    assert len(no_transform_mp(partial_sum_mp(basel_series, 10))) == 10
    assert len(Aitken_transform_mp(partial_sum_mp(basel_series, 10))) == 8
    assert len(Richardson_transform_mp(partial_sum_mp(basel_series, 10))) == 5
    assert len(Epsilon_transform_mp(partial_sum_mp(basel_series, 10))) == 8
    assert len(G_transform_mp(partial_sum_mp(basel_series, 10))) == 7

def test_simple_acceleration_mp():
    n, acel = emsum(basel_series, no_transform_mp, error=0.1)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n

    n, acel = emsum(basel_series, no_transform_mp, error=0.01)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n


if __name__ == '__main__':
    test_partial_sum_np()
    test_len_transformations_np()
    test_simple_acceleration_np()

    test_partial_sum_mp()
    test_len_transformations_mp()
    test_simple_acceleration_mp()
