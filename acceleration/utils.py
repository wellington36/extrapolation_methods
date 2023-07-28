from mpmath import log, exp

class LogNumber:
    def __init__(self, sign, num):
        self.sign = sign
        self.num = num
    
    def __add__(self, other):
        if type(other) == LogNumber:
            max_num = max([self.num, other.num])

            if self.sign == other.sign and self.num == max_num:
                return LogNumber(self.sign, max_num + log(exp(self.num - max_num) + exp(other.num - max_num)))
            else:
                if self.sign == other.sign:
                    return LogNumber(other.sign, max_num + log(exp(self.num - max_num) + exp(other.num - max_num)))
                elif self.num == max_num:
                    return LogNumber(self.sign, max_num + log(exp(self.num - max_num) - exp(other.num - max_num)))
                else:
                    return LogNumber(other.sign, max_num + log(exp(other.num - max_num) - exp(self.num - max_num)))

        else:
            return LogNumber(self.sign, self.num + other)
    
    def __sub__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign, self.num) + LogNumber(other.sign * -1, other.num)
        else:
            return LogNumber(self.sign, self.num - other)
    
    def __mul__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num + other.num)
        else:
            if other < 0:
                return LogNumber(self.sign * -1, self.num * other * (-1))
            else:
                return LogNumber(self.sign, self.num * other)
    
    def __truediv__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num / other.num)
        else:
            if other < 0:
                return LogNumber(self.sign * -1, self.num / (other * -1))
            else:
                return LogNumber(self.sign, self.num / other)
    
    def __neg__(self):
        return LogNumber(self.sign * -1, self.num)
    
    def __pow__(self, other):
        if type(other) == int:
            return LogNumber(self.sign ** other, self.num ** other)
        else:
            return NameError("Not implemented")
    
    def __eq__(self, other):
        if type(other) == LogNumber:
            return self.sign == other.sign and self.num == other.num
        else:
            return self.sign == 1 and self.num == other
    
    def __lt__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                return self.num < other.num
            else:
                return self.sign == -1
        else:
            return self.sign == -1
    
    def __gt__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                return self.num > other.num
            else:
                return self.sign == 1
        else:
            return self.sign == 1
    
    def __le__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                return self.num <= other.num
            else:
                return self.sign == -1
        else:
            return self.sign == -1
    
    def __ge__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                return self.num >= other.num
            else:
                return self.sign == 1
        else:
            return self.sign == 1

    def value(self):
        if self.sign == -1:
            return ('-', self.num)
        else:
            return ('+', self.num)


def create_lognumber(number):
    if number < 0:
        return LogNumber(-1, log(-number))
    else:
        return LogNumber(1, log(number))

if __name__ == '__main__':
    
    print('LogNumber class')

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

    a = create_lognumber(-1)
    b = create_lognumber(-2)
    c = create_lognumber(-0.25)
    d = create_lognumber(0)
    e = create_lognumber(5)

    ### Debug ###
    V = create_lognumber(0)
    print((V).value()[0], exp((V).value()[1]))

    V = a * d
    print((V).value()[0], exp((V).value()[1]))

    ### Test operators ###
    assert check_lognumber((a + b), create_lognumber(-3))
    assert check_lognumber((a + c), create_lognumber(-1.25))
    assert check_lognumber((a + d), create_lognumber(-1))
    assert check_lognumber((a + e), create_lognumber(4))
    
    assert check_lognumber((a - b), create_lognumber(1))
    assert check_lognumber((a - c), create_lognumber(-0.75))
    assert check_lognumber((a - d), create_lognumber(-1))
    assert check_lognumber((a - e), create_lognumber(-6))

    assert check_lognumber((a * b), create_lognumber(2))
    assert check_lognumber((a * c), create_lognumber(0.25))
    assert check_lognumber((a * d), create_lognumber(0))
    assert check_lognumber((a * e), create_lognumber(-5))

    assert a / b == LogNumber(1, 0.5)
    assert a / c == LogNumber(1, 4)
    assert a / e == LogNumber(-1, 0.2)

    assert a ** 2 == LogNumber(1, 1)
    assert a ** 1 == LogNumber(-1, 1)
    assert a ** 0 == LogNumber(1, 1)
    assert a ** -1 == LogNumber(-1, 1)

    assert a == LogNumber(-1, 1)
    assert b == LogNumber(-1, 2)

    assert a < b
    assert a <= b
    assert a <= a
    assert b > a
    assert b >= a

    assert (- b * e - e ** 2) == LogNumber(-1, 15)
    assert (c / e + a ** 2) == LogNumber(1, 0.95)
