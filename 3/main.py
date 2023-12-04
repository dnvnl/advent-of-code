#!/usr/bin/python3

import re

def search_char(b, e, n):
    f=False
    for p in range(max(0, min(li, b)), max(0, min(li, e))):
        if i[p] !='.':
            f = True
        if i[p] == '*':
            f=True
            if gs.get(p):
                gs[p].append(n.group())
            else:
                gs[p] = [n.group()]
    return f

with open('3/input.txt', 'r') as f:
    l = f.readlines()
    i = ''.join([i.split('\n')[0] for i in l])
    l = len(l[0])-1
    li = len(i)

r = re.compile(r'(\d{1,3})')

gs={}
s1, s2 = 0, 0

m = r.finditer(i)
for n in m:
    sb = False
    sc = ''
    (b, e) = n.span()
    if b%l==0:
        sb = sb or search_char(b-l, e-l+1, n)
        sb = sb or search_char(e, e+1, n)
        sb = sb or search_char(b+l, e+l+1, n)
    if e%l==0:
        sb = sb or search_char(b-l-1, e-l, n)
        sb = sb or search_char(b-1, b, n)
        sb = sb or search_char(b+l-1, e, n)
    if b%l!=0 and e%l!=0:
        sb = sb or search_char(b-l-1, e-l+1, n)
        sb = sb or search_char(b-1, b, n)
        sb = sb or search_char(e, e+1, n)
        sb = sb or search_char(b+l-1, e+l+1, n)

    if sb:
        s1+=int(n.group())


for g in gs:
    if len(gs[g])!=2:
        continue
    s2+=int(gs[g][0])*int(gs[g][1])

print('Answer 1 : {}'.format(str(s1)))
print('Answer 2 : {}'.format(str(s2)))
