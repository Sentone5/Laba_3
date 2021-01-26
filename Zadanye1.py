#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С клавиатуры вводится натуральное число n. В зависимости от значения остатка r при
# делении числа n на 7 вывести на экран число n в виде n = 7*k + r . Если r = 0 , то
# вывести на экран n = 7*k .

if __name__ == '__main__':
    n = int(input("Введите натуральное число n "))

    if n % 7 == 0:
        print("{} = 7*k".format(n))

    else:
        r = n % 7
        print("{} = 7*k + {}".format(n, r))
