# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from itertools import count
from random import sample


def numList(count):
    list = sample(range(1, count * 2), count)
    print(list)
    numSum = 0
    for i in range(0, count, 2):
        numSum +=list[i]
        i+=1
    print(numSum)


numList(int(input()))
