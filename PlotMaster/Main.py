import csv
from Plot import xyplot

s = '/Users/nalmog/Desktop/PreferentialMergeData/plots/SWA_e_cumulative.csv'
f = open(s, 'rU')

l1 = []
l2 = []
l3 = []

c = 0
for l in f:
    l = l.split(',')
    c+=1
    if(c==1):
        continue
    l1.append(l[0])
    l2.append(l[1])
    l3.append(l[2])

l1 = l1[0:10]
l2 = l2[0:10]
l3 = l3[0:10]

xyplot(l1,l2, "e")
xyplot(l1,l3, "u")
xyplot(l1,l1, "t")

print l1
print l2
print l3