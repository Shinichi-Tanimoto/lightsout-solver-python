#coding: utf-8

class F2:

    """
    標数2の体のクラス
    """

    def __init__(self, val):
        self.__value = val % 2

    def __add__(self, other):
        if not isinstance(other, F2):
            raise Exception("F2クラス以外のクラスとの演算はできません。")
        value = (self.__value + other.__value) % 2
        return F2(value)

    def __sub__(self, other):
        if not isinstance(other, F2):
            raise Exception("F2クラス以外のクラスとの演算はできません。")
        value = (self.__value - other.__value) % 2
        return F2(value)

    def __mul__(self, other):
        if not isinstance(other, F2):
            raise Exception("F2クラス以外のクラスとの演算はできません。")
        value = (self.__value * other.__value) % 2
        return F2(value)

    def  __div__(self, other):
        if not isinstance(other, F2):
            raise Exception("F2クラス以外のクラスとの演算はできません。")
        elif other.__value % 2 == 0:
            raise Exception("0では割れません。")
        return F2(other.__value)

    def __rmul__(self, other):
        if not isinstance(other, F2) and not isinstance(other, int):
            raise Exception("F2, intクラス以外のクラスとの演算はできません。")
        value = (self.__value * other) % 2
        return F2(value)

    def __str__(self):
        return str(self.__value)

    def __eq__(self, other):
        if not isinstance(other, F2):
            return False
        else:
            return self.__value == other.__value

if __name__ == '__main__':
    print F2(1) + F2(0)
    print F2(1) - F2(1)
    print F2(1) * F2(1)
    print F2(0) / F2(1)
    print 2 * F2(1)
    print F2(1) == F2(0)
