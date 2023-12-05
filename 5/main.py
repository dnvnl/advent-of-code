#!/usr/bin/python3

with open('5/input.txt', 'r') as f:
    l = f.readlines()

l = ''.join(l)

ps = l.split('\n\n')

w = [int(n) for n in ps[0].split(':')[1].split()]

for p in ps[1:]:
    m = [[int(n) for n in x.split()] for x in p.split('\n')[1:]]
    nw=[]
    for v in w:
        y=False
        for n in m:
            if n==[]:
                continue
            if v>=n[1] and v<n[1]+n[2]:
                nw.append(v+(n[0]-n[1]))
                y=True
                break
        if not y:
            nw.append(v)
    w=nw
    print(w)

s1=min(w)
s2=0

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
