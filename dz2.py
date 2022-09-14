# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите вещественное число: '))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(sum)




# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('N = '))
f=1
for i in range(1, N+1):
    f = f*i
    print(f, end = ' ')




# 3) Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. (1+1/n)^n

n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + round((1+1/i)**i, 2)
print(sum)




# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
N = int(input())
list = []
for i in range (N):
    list.append(randint(-N, N))
print(list)

fname = input('file')
f = open(fname, 'w')
while True:
    s = input()
    if s == ' ':
        break
    f.write(s+'\n')
f.close

result = 1
f = open(fname, 'r')
for i in f:
    if i == ' ':
        break
    result *= list[int(i)]
f.close()
print(result)


    

# 5) Реализуйте алгоритм перемешивания списка.
list = [1,3,5,23,53]
import random
for i in range(len(list)-1, 0 , -1):
    j = random.randint(0 , i+1)
    list[i], list[j] = list[j], list[i]
print(list)
