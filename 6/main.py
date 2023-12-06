#!/usr/bin/python3

from math import ceil

with open('6/input.txt', 'r') as f:
    l = f.readlines()

t = [int(x) for x in l[0].split(':')[1].split()]
d = [int(x) for x in l[1].split(':')[1].split()]

s1, s2 = 1, 1

for i in range(len(t)):
    s = 0
    for v in range(t[i]):
        r = v*(t[i]-v)
        if r>d[i]:
            s+=1
    s1*=s

t = [int(''.join(l[0].split(':')[1].split()))]
d = [int(''.join(l[1].split(':')[1].split()))]

for i in range(len(t)):
    s = 0
    for v in range(t[i]):
        r = v*(t[i]-v)
        if r>d[i]:
            s+=1
    s2*=s

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
        