# Домашнее Задание № 1
# Задача :
# 1. Перезаписать все три пройденные алгоритмы в ООП
# стиль ( используя конструктор init и обращение к
# атрибуту через self )
# 2. К таким темам относятся Бинарное дерево ,
# Сортировка Пузырьком , Быстрая сортировка


class R:
    def __init__(self, array) -> None:
        self.array = array

    def bubble_sort(self): # поиск пузырь
        swapper = False
        for i in range(len(self.array)-1, 0, -1):
            for k in range(i):
                if self.array[k] > self.array[k + 1]:
                    self.array[k], self.array[k + 1] = self.array[k + 1], self.array[k]
                    swapper = True
            if swapper:
                swapper = False
            else:
                break
        return self.array

    def quick_sort(self, array=None):
        if array == None:
            array = self.array
        if len(array) <= 1:
            return array
        element = array[0]

        left = list(filter(lambda num: num < element, array))
        center = [nums for nums in array if nums == element]
        right = list(filter(lambda num: num > element, array))

        return self.quick_sort(left) + center + self.quick_sort(right)

    def b_tree(self, number):
        self.quick_sort(self.array)

        mid = len(self.array) // 2
        min = 0
        max = len(self.array) - 1

        while number != self.array[mid] and min < max:
            if number > self.array[mid]:
                min = mid + 1
            else:
                max = mid - 1
            mid =(max + mid) // 2
        if max < min:
            return "No value"
        else:
            return mid 

f = R([1, 4, 3, 11, 5, 50, 42])

print(f.b_tree(50))
                 
        