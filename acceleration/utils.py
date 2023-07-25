from mpmath import mp, log, mpf

class LogNumber:
    def __init__(self, sign, num):
        self.sign = sign
        self.num = num
    
    def __add__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                return LogNumber(self.sign, self.num + other.num)
            else:
                if self.num > other.num:
                    return LogNumber(self.sign, self.num - other.num)
                else:
                    return LogNumber(other.sign, other.num - self.num)
        else:
            return LogNumber(self.sign, self.num + other)
    
    def __sub__(self, other):
        if type(other) == LogNumber:
            if self.sign == other.sign:
                if self.num > other.num:
                    return LogNumber(self.sign, self.num - other.num)
                else:
                    return LogNumber(other.sign, other.num - self.num)
            else:
                return LogNumber(self.sign, self.num + other.num)
        else:
            return LogNumber(self.sign, self.num - other)
    
    def __mul__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num * other.num)
        else:
            if other < 0:
                return LogNumber(self.sign * -1, self.num * other)
            else:
                return LogNumber(self.sign, self.num * other)
    
    def __truediv__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num / other.num)
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

    a = LogNumber(-1, mpf('0.423581381'))
    b = LogNumber(-1, mpf('0.431631581'))
    c = LogNumber(-1, mpf('0.438105068'))
    d = LogNumber(-1, mpf('0.44'))

    print(a.value())
    print(b.value())
    print(c.value())
    print(d.value())

    # t0 = aux[i+3]*aux[i+1] +  aux[i] * aux[i+2] + aux[i+1] * aux[i+2] - aux[i+2]**2 - aux[i+3]*aux[i] - aux[i+1]**2


    print((d * b).value())
    print((a * c).value())
    print((b * c).value())
    #print((- ).value())
    print((a + c).value())
    print((a + c).value())