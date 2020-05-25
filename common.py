##
# @file
# @brief    Файлик с ништяками, которые могут потребоваться внезапно
#           и должны быть под рукой всегда.
# @author   Danya0x07
#

##
# @brief    Определяет простость числа.
# @param n  Проверяемое число.
#
# @return True, если число простое,
# @return False в противном случае.
# @todo Оптимизировать границу цикла поиска, там вроде до корня как-то можно,
#       но я забыл как.
#
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True
