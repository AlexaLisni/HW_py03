#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
from random import sample


def DecToBin(num):
    res = []
    i = -1
    while num > 1:
        a = num % 2
        res.insert(i,a)
        i-=1
        num=num//2  
    res.insert(0,1) 
    for i in range(len(res)):
        b=res[i]  
        print(b,end='')



DecToBin(int(input()))

