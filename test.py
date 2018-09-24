from itertools import product

list1 = [1,2,3,4,5,6]
a = ['trololo']
b = ['chupacabra']
res = product(list1,a,b)
print(list(res))
