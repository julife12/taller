def entre_0_5(x,y):
    if 5>x>0 and 5>y>0:
        return True
    else:
        return False

a=int(input("digite un numero"))
b=int(input("digite un numero"))
x=entre_0_5(a,b)
print(x)