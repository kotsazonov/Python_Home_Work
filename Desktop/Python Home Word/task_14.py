#Задача 14: Требуется вывести все целые степени двойки
#(т.е. числа вида 2**k), не превосходящие числа N.

def powers_of_two(N):
    k = 0
    power = 1

    while power <= N:
        print(power)
        k += 1
        power = 2 ** k

N = 100

powers_of_two(N)
