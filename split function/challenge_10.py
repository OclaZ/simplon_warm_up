from functools import reduce
list=[1,2,3,4,5]
def produit(x,y):
    return x*y 
s=reduce(produit,list)
print(s)