# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fib(num):
    list = [0,1]
    i = 1 
    while i < num:
        list.append(list[i]+list[i-1])
        i+=1
    return list
def NegaFib (num):
    list = [1,-1]
    i = 1
    while i < num - 1:
        list.append(list[i-1]-list[i])
        i+=1
    return list

def Answer(negafib,fib):
    list = []
    for i in range(len(negafib)):
        list.append(negafib[-(i+1)]) 
    for i in range(len(fib)):
        list.append(fib[i])
    return list

def Test():
    res_do = Answer(NegaFib(8),Fib(8))
    res_need = [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    if res_do == res_need: 
        print("Autotest successful")
    else:
        print("Not OK")


Test()
num = int(input("Input N "))
res = Answer(NegaFib(num),Fib(num))
print(res)



