import random
import math


def score(n: float) -> int:
    return 1 if n > 0 else 0


def monte_carlo(n: int, f, a: float, b: float) -> list:
    items_sum = [0]

    for _ in range(n):
        x = random.random() * (b - a) + a
        y = f(x)
        
        items_sum.append(items_sum[-1] + y)
    return items_sum


##### Methods ----------------------------------------------------------------
def aceleration_A(items_sum: list) -> list:
    acel = [0]

    for i in range(1, len(items_sum) - 2):
        acel.append((items_sum[i] * items_sum[i+2] - items_sum[i+1]**2) / (items_sum[i+2] - 2* items_sum[i+1] + items_sum[i]))
    
    return acel

def aceleration_R(items_sum: list, p=1) -> list:
    acel = [0]

    for i in range(1, int(len(items_sum) / 2)):
        acel.append(items_sum[2*i] + (items_sum[2*i] - items_sum[i]) / (2**p - 1))
    
    return acel

def aceleration_Epsilon(items_sum: list) -> list:
    aux = [0]
    acel = [0]

    for i in range(1, len(items_sum)):
        aux.append(1/(items_sum[i] - items_sum[i-1]))

    for i in range(1, len(items_sum)):
        acel.append(items_sum[i] + 1/(aux[i] - aux[i-1]))
    
    return acel

def aceleration_G(items_sum: list) -> list:
    # r is the ratio of the two consecutive terms of the sequence

    acel = [0]

    for i in range(1, len(items_sum)-1):
        acel.append(items_sum[i-1] - (items_sum[i] - items_sum[i-1])*(items_sum[i+1] - items_sum[i])/(items_sum[i+1] - 2 * items_sum[i] + items_sum[i-1]))
    
    return acel


##### Test -------------------------------------------------------------------

def f(n: float):
    return math.e ** (math.e ** n)

if __name__ == "__main__":
    Tests = 10_000
    N = 1_000
    a = 0
    b = 2
    L = 261.992431757597046451899   # Limit of the integral (remember: 261.992431757597046451899)

    score_vector = {'A': 0, 'R1': 0, 'Rdecimo': 0, 'R10': 0, 'G': 0, 'Epsilon': 0}

    for i in range(Tests):


        items_sum = monte_carlo(N, f, a, b)
        #print(f"Sem aceleração:         {items_sum[-1]/N}")
        #print(f"Com o método A:         {aceleration_A(items_sum)[-1]/N}")
        #print(f"Com o método R1:         {aceleration_R(items_sum, 1)[-1]/N}")
        #print(f"Com o método Rdecimo:         {aceleration_R(items_sum, 1/10)[-1]/N}")
        #print(f"Com o método R10:         {aceleration_R(items_sum, 10)[-1]/N}")
        #print(f"Com o método G:         {aceleration_G(items_sum)[-1]/N}")
        #print(f"Com o método Epsilon:   {aceleration_Epsilon(items_sum)[-1]/N}")

        error_A = abs(L - items_sum[-1]/N) - abs(L - aceleration_A(items_sum)[-1]/N)
        error_R1 = abs(L - items_sum[-1]/N) - abs(L - aceleration_R(items_sum, 1)[-1]/N)
        error_Rdecimo = abs(L - items_sum[-1]/N) - abs(L - aceleration_R(items_sum, 1/10)[-1]/N)
        error_R10 = abs(L - items_sum[-1]/N) - abs(L - aceleration_R(items_sum, 10)[-1]/N)
        error_G = abs(L - items_sum[-1]/N) - abs(L - aceleration_G(items_sum)[-1]/N)
        error_Epsilon = abs(L - items_sum[-1]/N) - abs(L - aceleration_Epsilon(items_sum)[-1]/N)

        score_vector['A'] += score(error_A)
        score_vector['R1'] += score(error_R1)
        score_vector['Rdecimo'] += score(error_Rdecimo)
        score_vector['R10'] += score(error_R10)
        score_vector['G'] += score(error_G)
        score_vector['Epsilon'] += score(error_Epsilon)

    print(f"Score A: {score_vector['A']}")
    print(f"Score R (p=1): {score_vector['R1']}")
    print(f"Score R (p=1/10): {score_vector['Rdecimo']}")
    print(f"Score R (p=10): {score_vector['R10']}")
    print(f"Score G: {score_vector['G']}")
    print(f"Score Epsilon: {score_vector['Epsilon']}")

    