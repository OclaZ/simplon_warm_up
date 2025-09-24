tab=[1,5,2,6,8,3,14,22,15,11]
def filtring(n):
    if n%2!=0:
        return True
    else:
        return False

impaires=list(filter(filtring,tab))
print(impaires)

