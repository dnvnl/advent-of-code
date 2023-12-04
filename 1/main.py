#!/usr/bin/python3

import re

def f(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    try:
        return int(s)
    except ValueError:
        return a.index(s)

with open('1/input.txt', 'r') as f:
    l = f.readlines()

r1 = re.compile(r'(?=(\d))')
r2 = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

n1, n2, s1, n3, n4, s2 = 0, 0, 0, 0, 0, 0

def f(s):
    names_to_values = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    try:
        return int(s)
    except:
        return names_to_values.index(s)

for i in l:
    m1 = r1.findall(i)
    n1, n2 = int(m1[0]), int(m1[-1])

    s1 += (n1*10 + n2)

    m2 = r2.findall(i)
    n3, n4 = f(m2[0]), f(m2[-1])

    s2 += (n3*10 + n4)

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
