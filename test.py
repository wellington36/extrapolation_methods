import math
from acceleration import Aitken_tranform, Richardson_transform, Epsilon_transfom, G_transform

def square_series(n: int) -> list:
    series = [1.0]

    for i in range(2, n+1):
        series.append(series[-1] + 1/(i)**2)
    
    return series

if __name__ == "__main__":
    for i in range(1, 6):
        initial_series = abs(math.pi**2 / 6 - square_series(10**i)[-1])
        acceration_series = abs(math.pi**2 / 6 - Aitken_tranform(square_series(10**i))[-1])

        print(f"Error in initial series with n={10**i}: {initial_series}")
        print(f"Errro in acceleration series with n={10**i}: {acceration_series}")
        print("\n")

    print(Epsilon_transfom(square_series(10)))
