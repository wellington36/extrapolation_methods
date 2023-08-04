from mpmath import log, exp, mp
import math

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
            return LogNumber(self.sign, self.num) + create_lognumber(other)
    
    def __sub__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign, self.num) + LogNumber(other.sign * -1, other.num)
        else:
            return LogNumber(self.sign, self.num) - create_lognumber(other)
    
    def __mul__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num + other.num)
        else:
            return LogNumber(self.sign, self.num) * create_lognumber(other)
    
    def __truediv__(self, other):
        if type(other) == LogNumber:
            return LogNumber(self.sign * other.sign, self.num - other.num)
        else:
            return LogNumber(self.sign, self.num) / create_lognumber(other)
    
    def __neg__(self):
        return LogNumber(self.sign * -1, self.num)
    
    def __pow__(self, other):
        if type(other) == int:
            return LogNumber(self.sign ** other, self.num * other)
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

    def exp(self, precision=53):
        if precision != 53:
            mp.prec = precision
            
            return self.sign * exp(self.num)
        else:
            return self.sign * math.exp(self.num)

    def value(self):
        return (self.sign, self.num)


def create_lognumber(number, lib='mpmath'):
    if lib == 'mpmath':
        if number < 0:
            return LogNumber(-1, log(-number))
        else:
            return LogNumber(1, log(number))
    elif lib == 'math':
        if number < 0:
            return LogNumber(-1, math.log(-number))
        else:
            return LogNumber(1, math.log(number))
    else:
        raise NameError("Not implemented")

if __name__ == '__main__':
    
    print('LogNumber class')