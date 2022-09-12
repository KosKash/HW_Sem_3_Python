# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: 
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Summ_pair(list):
    res_list = []
    if len(list) % 2 == 0:
        i = 0
        k = -1
        while i < len(list)/2:
            res_list.append(list[i]*list[k])
            i+=1
            k-=1
        return res_list
    else:
        i = 0
        k = -1
        while i <= ((len(list)/2)):
            res_list.append(list[i]*list[k])
            i+=1
            k-=1
        return res_list

num_list = [2,3,4,4,3,2]
num_list_2 = [2,3,4,3,2]
res = Summ_pair(num_list)
print('{} : {} '.format(num_list,res))
res2 = Summ_pair(num_list_2)
print('{} : {} '.format(num_list_2,res2))



