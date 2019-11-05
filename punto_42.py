n=int(input("ingrese el numero que quiere evaluar"))
if n/100000>=1:
    print("el numero tiene 6 cifras ")
elif n/10000>=1:
    print("el numero tiene 5 cifras ")
elif n/1000>=1:
    print("el numero tiene 4 cifras ")
elif n/100>=1:
    print("el numero tiene 3 cifras ")
elif n/10>=1:
    print("el numero tiene 2 cifras ")
elif n/1>=1:
    print("el numero tiene 1 cifras ")