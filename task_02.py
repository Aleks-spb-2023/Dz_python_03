#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
def getproizindexarray(x):
    arr = []
    a = list(reversed(x))
    if len(a) % 2 == 0:
        a = a[:len(a) //2]
    else:
        a = a[:len(a) //2 + 1]
    arr = []
    for i in range(len(a)):
        arr.append(a[i] * x[i])
    return arr
e = [2, 3, 4, 5, 6]
print(getproizindexarray(e))