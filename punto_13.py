a=int(input("digite el primer numeoro: "))
b=int(input("digite el segundo termino: "))
c=int(input("digite el tercer termino: "))
if a>b and b>c:
    print("el mayor fue: ", a, "el menor fue: ", c)
elif a>b and b<c:
    print("el mayor fue: ", a, "el menor fue: ", b)
elif b>a and a>c:
    print("el mayor fue: ", b, "el menor fue: ", c)
elif b>a and a<c:
    print("el mayor fue: ", b, "el menor fue: ",a)