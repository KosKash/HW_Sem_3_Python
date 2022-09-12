# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def to_bit(num):
    list = []
    while num > 0:
        a = num%2
        list.append(a)
        num //= 2
    rev = []
    for i in range(len(list)):
        rev.append(list[-(i+1)])
    return rev

def to_string (list):
    str1 = ''
    for i in list:
        str1+=str(i)
    return str1

num = int(input())
res = to_string(to_bit(num))
print('{} ==> {}'.format(num,res))