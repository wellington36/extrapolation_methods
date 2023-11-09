from extrapolation.esum import (
    esum,
    acelsum,
    partial_sum_list,
    partial_sum_mp,
    no_transform,
    Aitken_transform,
    Richardson_transform,
    Epsilon_transform,
    G_transform,
    Levin_t_transform,
    Levin_u_transform,
    Levin_v_transform
)
from extrapolation.utils import create_lognumber
from mpmath import exp, log, mp


#################### Auxiliar function ####################
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

#################### TESTS lists ####################

def test_partial_sum_list():
    array = partial_sum_list(basel_series, 4)

    assert type(array) == list
    assert len(array) == 4
    assert equivalence(array[0].exp(), 1)
    assert equivalence(array[1].exp(), 5/4)
    assert equivalence(array[2].exp(), 49/36)
    assert equivalence(array[3].exp(), 205/144)

def test_len_transformations_list():
    assert len(no_transform(partial_sum_list(basel_series, 10), lib='math')) == 10
    assert len(Aitken_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(Richardson_transform(partial_sum_list(basel_series, 10), lib='math')) == 5
    assert len(Epsilon_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(G_transform(partial_sum_list(basel_series, 10), lib='math')) == 7
    assert len(Levin_t_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(Levin_u_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(Levin_v_transform(partial_sum_list(basel_series, 10), lib='math')) == 8

def test_simple_acceleration_list():
    n, acel = esum(basel_series, "None", error=0.1)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n

    n, acel = esum(basel_series, "Aitken", error=0.01)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n-2

    acel = acelsum(basel_series, "None", n=10, logarithm=False)
    assert type(acel) == list
    assert type(acel[-1]) == float
    assert len(acel) == 10

    acel = acelsum(basel_series, "Aitken", n=10, logarithm=False)
    assert type(acel) == list
    assert type(acel[-1]) == float
    assert len(acel) == 8

#################### TESTS mpmath ####################
def test_partial_sum_mp():
    array = partial_sum_mp(basel_series, 4)

    assert type(array) == list
    assert len(array) == 4
    assert equivalence(array[0].exp(), 1)
    assert equivalence(array[1].exp(), 5/4)
    assert equivalence(array[2].exp(), 49/36)
    assert equivalence(array[3].exp(), 205/144)


def test_len_transformations_mp():
    mp.prec = 100

    assert len(no_transform(partial_sum_mp(basel_series, 10), lib='mpmath')) == 10
    assert len(Aitken_transform(partial_sum_mp(basel_series, 10), lib='mpmath')) == 8
    assert len(Richardson_transform(partial_sum_mp(basel_series, 10), lib='mpmath')) == 5
    assert len(Epsilon_transform(partial_sum_mp(basel_series, 10), lib='mpmath')) == 8
    assert len(G_transform(partial_sum_mp(basel_series, 10), lib='mpmath')) == 7
    assert len(Levin_t_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(Levin_u_transform(partial_sum_list(basel_series, 10), lib='math')) == 8
    assert len(Levin_v_transform(partial_sum_list(basel_series, 10), lib='math')) == 8

def test_simple_acceleration_mp():
    n, acel = esum(basel_series, "None", error=0.1, precision=100)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n

    n, acel = esum(basel_series, "Aitken", error=0.01, precision=100)
    assert type(n) == int
    assert type(acel) == list
    assert len(acel) == n-2

    acel = acelsum(basel_series, "None", n=10, logarithm=False, precision=100)
    assert type(acel) == list
    assert type(acel[-1]) == mp.mpf
    assert len(acel) == 10

    acel = acelsum(basel_series, "Aitken", n=10, logarithm=False, precision=100)
    assert type(acel) == list
    assert type(acel[-1]) == mp.mpf
    assert len(acel) == 8


#################### TESTS transformations in acelsum and esum ####################
def test_transformation_in_acelsum():
    assert type(acelsum(basel_series, "None", n=10)) == list
    assert type(acelsum(basel_series, "Aitken", n=10)) == list
    assert type(acelsum(basel_series, "Richardson", n=10)) == list
    assert type(acelsum(basel_series, "Epsilon", n=10)) == list
    assert type(acelsum(basel_series, "G", n=10)) == list
    assert type(acelsum(basel_series, "Levin-t", n=10)) == list
    assert type(acelsum(basel_series, "Levin-u", n=10)) == list
    assert type(acelsum(basel_series, "Levin-v", n=10)) == list

def test_transformation_in_esum():
    assert type(esum(basel_series, "None", error=0.1)) == tuple
    assert type(esum(basel_series, "Aitken", error=0.1)) == tuple
    assert type(esum(basel_series, "Richardson", error=0.1)) == tuple
    assert type(esum(basel_series, "Epsilon", error=0.1)) == tuple
    assert type(esum(basel_series, "G", error=0.1)) == tuple
    assert type(esum(basel_series, "Levin-t", error=0.1)) == tuple
    assert type(esum(basel_series, "Levin-u", error=0.1)) == tuple
    assert type(esum(basel_series, "Levin-v", error=0.1)) == tuple

if __name__ == '__main__':
    test_partial_sum_list()
    test_len_transformations_list()
    test_simple_acceleration_list()

    test_partial_sum_mp()
    test_len_transformations_mp()
    test_simple_acceleration_mp()

    test_transformation_in_acelsum()
    test_transformation_in_esum()