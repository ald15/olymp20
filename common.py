##
# @file
# @brief    Файлик с ништяками, которые могут потребоваться внезапно
#           и должны быть под рукой всегда.
# @author   Danya0x07, Werther
#

##
# @brief    Определяет простость числа.
# @param n  Проверяемое число.
#
# @return True, если число простое,
# @return False в противном случае.
# 
#
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True
