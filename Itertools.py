from itertools import product

a=list(map(int, input().split()))
b=list(map(int, input().split()))
print(' '.join([str(x) for x in list(product(a,b))]))

#print((int(numA), int(numB)) for numA in a for numB in b)

#s = ""
#for numA in a:
#    for numB in b:
#        s += str((int(numA), int(numB))) + " "
# print(s)