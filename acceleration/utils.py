from mpmath import mp, log

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
            return LogNumber(self.sign, self.num * other)
    
    def __truediv__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num / other.num)
        else:
            return LogNumber(self.sign, self.num / other)
    
    def __pow__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num ** other.num)
        else:
            return LogNumber(self.sign, self.num ** other)

    
    def return_value(self):
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

    a = create_lognumber(2)
    b = a * 2

    print(a.return_value())
    print(b.return_value())