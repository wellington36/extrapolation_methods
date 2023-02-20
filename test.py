import math
from acceleration import Aitken_tranform

def square_serie(n: int) -> list:
    # approx to math.pi**2 / 6

    serie = [0]

    for i in range(1, n):
        serie.append(serie[-1] + 1/(i)**2)
    
    return serie

if __name__ == "__main__":
    print(abs(math.pi**2 / 6 - square_serie(10000)[-1]))
    print(abs(math.pi**2 / 6 - Aitken_tranform(square_serie(10000))))