# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(f'Список : {arr}')
# minn, maxx = 5, 10
minn = int(input('Введите минимум диапазона: '))
maxx = int(input('Введите максимум диапазона: '))
res = list()
for i in range(len(arr)):
    if (minn <= arr[i] <= maxx):
        res.append(i)
print(res)


# # Решение на коленке
# my_list_index_2 = list()

# for i in range(len(your_list)):
#     if minn <= (your_list[i]) <= maxx:
#         my_list_index_2.append(i)
# print(my_list_index_2)