import math
a = input().split()
n = int(a[0])
A = int(a[1])
b = int(a[2])
c = int(a[3])
d = int(a[4])
seta = math.ceil(n / A)
setc = math.ceil(n / c)
costa = seta * b
costb = setc * d
if costa < costb:
    print(costa)
elif costb < costa:
    print(costb)
else:
    print(costa)