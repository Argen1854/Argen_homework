# Задание № Алгоритм
# 1. Даны два значения ( numbers , desired_sum )
# 2. Первая это список из чисел
# 3. Вторая это число которое должно получиться из двух чисел
# Смысл :
# Нужно сделать так чтобы возвращался индекс двух чисел которые в сумме возвращают желаемую сумму
# Например есть список из таких чисел [2, 7, 11, 15] желаемая сумма является число 9 , значит должен
# возвращаться индекс [0, 1] потому что только сумма этих двух чисел является желаемой
# Подсказка : Нужно использовать циклы for
# ДОП домашка :
# Сделать в классахdd
 
num = 9
list_num = [2, 7, 3, 7, 2, 2]

class R:
    def __init__(self, lst) -> None:
        self.lst = lst
    def find_i(self, num):
        result = []
        for i in range(len(self.lst)):
            for k in range(i, len(self.lst)):
                if self.lst[i] + self.lst[k] == num:
                    result_i = (i, k)
                    result.append(result_i)
        
        return result

    
    
ara = R(list_num)
print(ara.find_i(num))

