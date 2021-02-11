d, g = map(int,input().split())
plist = []
clist = []

for _ in range(d):
    p, c = map(int,input().split())
    plist.append(p)
    clist.append(c)

sumlist = []
for i in range(d):
    sumnum = (i+1) * 100 * plist[i] + clist[i]
    sumlist.append(sumnum)

#途中までしか分からず、解説見ても分からず。