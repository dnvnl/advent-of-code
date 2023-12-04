#!/usr/bin/python3

import re

def convert_arr_to_int(a):
    s = []
    for i in a:
        s.append(int(i))
    return s

with open('2/input.txt', 'r') as f:
    l = f.readlines()

rr = re.compile(r'(\d+) red')
rg = re.compile(r'(\d+) green')
rb = re.compile(r'(\d+) blue')

game, s1, s2 = 0, 0, 0

for i in l:
    r = max(convert_arr_to_int(rr.findall(i)))
    g = max(convert_arr_to_int(rg.findall(i)))
    b = max(convert_arr_to_int(rb.findall(i)))

    game+=1

    s2 += r*g*b

    if r>12 or g>13 or b>14:
        continue

    s1 += game

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
