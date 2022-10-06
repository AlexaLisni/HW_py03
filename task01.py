#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample
def numList(count,):
    list=sample(range(1, count * 2), count)
    print(list)
print(numList(int(input())))