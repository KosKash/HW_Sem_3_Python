#  Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#  Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from os import remove

def Find(list): 
    op_list = []
    for i in range(len(list)):
        x = float(list[i])
        while x > 1:
            x -=1
        op_list.append(round(x,3))
    op_list.remove(1)
    return op_list

def Min_max(list): 
    i = 0
    max = list[i]
    min = list[i]
    for i in range(len(list)):
        if list[i] > max: max = list[i]
    for i in range(len(list)):
        if list[i] < min: min = list[i]
    return min, max

num_list = [1.1, 1.2, 3.1, 5, 10.01]
nums = (Min_max(Find(num_list)))
res = nums[1] - nums[0]
print("{} ==> {}".format(num_list,res))


