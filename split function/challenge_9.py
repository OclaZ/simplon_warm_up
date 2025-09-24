a=[1,2,3,4,5]
b=[6,7,8,9,10]
def addition(x,y):
    return x+y

x=list(zip(a,b))
s=list(map(lambda p: addition(p[0],p[1]),x))
print(x)
print(s)

