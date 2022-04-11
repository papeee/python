import math
# a|x|+b = 0
x = []
a = [6,0]
b = -2
y = 0
z = 1
print ("Itseisarvoyhtälö |x| + b = 0")

if a[0] == b:
    x.append(z)
else:
    if b/a[0] < 0:
        if b/a[0] > 0:
            x.append(z)
            print (x[0])
        else:
            x.append(y)
            print (x[0])

if a[1] == b:
    x.append(z)
else:
    if a[1] != 0:
        if b/a[1] < 0:
            if b/a[1] > 0:
                x.append(y)
                print (x[1])
    else:
        x.append(z)
        print (x[1])

