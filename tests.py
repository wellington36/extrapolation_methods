from acceleration.esum import esum, no_transform_np, Richardson_transform_np, Aitken_transform_np, Epsilon_transform_np, G_transform_np, partial_sum_np
from acceleration.emsum import emsum, no_transform_mp, Richardson_transform_mp, Aitken_transform_mp, Epsilon_transform_mp, G_transform_mp, partial_sum_mp
from acceleration.utils import create_lognumber
from mpmath import exp, log
import numpy as np

def basel_series(n: int):
    return 1/(n)**2

def equivalence(a, b, epsilon=0.0001):
    if a == b:
        return True
    else:
        return abs(a - b) < epsilon
    
def check_lognumber(a, b):
    if equivalence(a.value()[1], b.value()[1]):
        return equivalence(a.value()[1], create_lognumber(0).value()[1]) or a.value()[0] == b.value()[0]
    else:
        return False

#################### TESTS utils ####################
def test_operations():
    a = create_lognumber(-1)
    b = create_lognumber(-2)
    c = create_lognumber(-0.25)
    d = create_lognumber(0)
    e = create_lognumber(5)

    ### Test operators ###
    ## Addition ##
    assert check_lognumber((a + b), create_lognumber(-3))
    assert check_lognumber((a + c), create_lognumber(-1.25))
    assert check_lognumber((a + d), create_lognumber(-1))
    assert check_lognumber((a + e), create_lognumber(4))

    assert check_lognumber((a + 2), create_lognumber(1))
    assert check_lognumber((a + (-2)), create_lognumber(-3))
    
    ## Subtraction ##
    assert check_lognumber((a - b), create_lognumber(1))
    assert check_lognumber((a - c), create_lognumber(-0.75))
    assert check_lognumber((a - d), create_lognumber(-1))
    assert check_lognumber((a - e), create_lognumber(-6))

    assert check_lognumber((a - 2), create_lognumber(-3))
    assert check_lognumber((a - (-2)), create_lognumber(1))

    ## Multiplication ##
    assert check_lognumber((a * b), create_lognumber(2))
    assert check_lognumber((a * c), create_lognumber(0.25))
    assert check_lognumber((a * d), create_lognumber(0))
    assert check_lognumber((a * e), create_lognumber(-5))

    assert check_lognumber((a * 2), create_lognumber(-2))
    assert check_lognumber((a * (-2)), create_lognumber(2))

    ## Division ##
    assert check_lognumber((a / b), create_lognumber(0.5))
    assert check_lognumber((a / c), create_lognumber(4))
    assert check_lognumber((a / e), create_lognumber(-0.2))

    assert check_lognumber((a / 2), create_lognumber(-0.5))
    assert check_lognumber((a / (-2)), create_lognumber(0.5))

    ## Negation ##
    assert check_lognumber((-a), create_lognumber(1))
    assert check_lognumber((-e), create_lognumber(-5))

    ## Power ##
    assert check_lognumber((a ** 2), create_lognumber(1))
    assert check_lognumber((a ** 1), create_lognumber(-1))
    assert check_lognumber((a ** 0), create_lognumber(1))
    assert check_lognumber((a ** -1), create_lognumber(-1))

    ### Test comparison operators ###
    assert (a == b) == False
    assert (a == c) == False

    assert a < b
    assert a <= b
    assert a <= a
    assert b > a
    assert b >= a

    ### Test return number ###
    assert equivalence(a.exp(), (-1) * exp(log(1)))
    assert equivalence(e.exp(), (+1) * exp(log(5)))

    ### Test properties ###
    assert check_lognumber((a + (-a)), create_lognumber(0))
    assert check_lognumber((a * (a**-1)), create_lognumber(1))
    assert check_lognumber((b + (-b)), create_lognumber(0))
    assert check_lognumber((b * (b**-1)), create_lognumber(1))
    assert check_lognumber((c + (-c)), create_lognumber(0))
    assert check_lognumber((c * (c**-1)), create_lognumber(1))
    assert check_lognumber((e + (-e)), create_lognumber(0))
    assert check_lognumber((e * (e**-1)), create_lognumber(1))

    ### Test examples ###
    assert check_lognumber((- b * e - e ** 2), create_lognumber(-15))
    assert check_lognumber((a * b * c * d * e), create_lognumber(0))
    assert check_lognumber((c / e + a ** 2), create_lognumber(0.95))
    assert check_lognumber((b + (-b)), create_lognumber(0))
    assert check_lognumber((b * (b**-1)), create_lognumber(1))

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
