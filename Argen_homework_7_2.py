# Домашнее Задание № 2
# Задача # легкий алгоритм
# Смысл задачи: Дается число и если это число можно читать с
# конца до начало и выходит также как и при обратном счете значит
# это число относится к универсальным числам
# 1. Дано число 343 и нужно работать с ним
# 2. Все числа с минусовым значением заведемо считаются не
# универсальными такие как -343

def ez_Algorithm_cheat(number):
    string = str(number)
    if (string[::-1]) == str(number):
        return True
    else:
        return False

def ez_Algorithm(number):
    if number // 100 == number % 10:
        return True
    else:
        return False


print(ez_Algorithm(343))
