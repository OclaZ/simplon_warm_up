a=[1,2,3,4,5]
b=[6,7,8,9,10]
def addition(x,y):
    return x+y
def sum(p):
    return p[0]+p[1]

x=list(zip(a,b))
s=list(map(lambda p: addition(p[0],p[1]),x))
s2=list(map(sum,x)) 
print(x)
print(s)
print(s2)

