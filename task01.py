# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from itertools import count
from random import sample


def numList(count):
    list = sample(range(1, count * 2), count)
    print(list)
    i = 0
    numSum = 0
    while i <= count:
        numSum += list[i]
        i += 2
    print(numSum)


numList(int(input()))
