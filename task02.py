#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample


def numList(count):
    list = sample(range(1, count * 2), count)
    print(list)
    j = -1
    mult= 1
    if(len(list)%2!=0):
        a = (len(list)//2)
        b = list.pop(a)
        result = [b]
        for i in range(len(list)):
            if i < len(list)//2:
                mult = list[i]*list[j]
                j-=1
                result.insert(i,mult)
    elif (len(list)%2==0):
        result =[]
        for i in range(len(list)):
            if i < len(list)//2:
                mult = list[i]*list[j]
                j-=1
                result.insert(i,mult)


    print(result)    
    


numList(int(input()))


