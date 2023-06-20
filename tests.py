from src.acceleration import acceleration, no_transform, Richardson_transform, Aitken_transform, Epsilon_transform, G_transform, partial_sum

def basel_series(n: int):
    return 1/(n)**2

def test_len_transformations():
    assert len(no_transform(partial_sum(basel_series, 10))) == 10
    assert len(Aitken_transform(partial_sum(basel_series, 10))) == 8
    assert len(Richardson_transform(partial_sum(basel_series, 10))) == 5
    assert len(Epsilon_transform(partial_sum(basel_series, 10))) == 8
    assert len(G_transform(partial_sum(basel_series, 10))) == 7


if __name__ == '__main__':
    test_len_transformations()