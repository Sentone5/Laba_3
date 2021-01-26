#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Через сколько дней спортсмен из задания 1 будет пробегать в день больше 15 км?

if __name__ == '__main__':
    Dist = 10
    while Dist < 15:
        Dist *= 1.1
    print(Dist)
