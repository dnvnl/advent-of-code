#!/usr/bin/python3

with open('4/input.txt', 'r') as f:
    l = f.readlines()

s1, s2 = 0, 0
o=[0]

for j, i in enumerate(l):
    if i=='':
        break
    if len(o) < j+2:
        o.append(1)
    s = 0
    c=0
    w = i.split(":")[1].split('|')[0].split()
    h = i.split(":")[1].split('|')[1].split()
    for n in h:
        if n in w:
            c+=1
            if s==0:
                s=1
            else:
                s=s*2
    for cc in range(1, c+1):
        if len(o) < (j+1+cc)+1:
            o.append(o[j+1]+1)
        else:
            o[j+1+cc] += o[j+1]
    s1+=s

s2=sum(o)

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
