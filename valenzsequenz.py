d = [2, 3, 8, 8, 2, 9, 3, 8, 3, 2]

print d,

valseq=1

while len(d) >0:
    d.sort()
    last=d.pop()
    if last>len(d):
        valseq=0
        break
    for i in range(len(d)-1, len(d)-last-1,-1):
        if d[i]>0:
            d[i]=d[i]-1
        else:
            valseq=0
if valseq==1:
    print " ist eine Valenzsequenz"
else:
    print " ist keine Valenzsequenz"
