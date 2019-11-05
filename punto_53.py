n=int(input("digite el inicio "))
m=int(input("digite el final "))
suma=0
if n>m:
    print("lo siento digite unos valores de modo que el primero sea el menor")
else:
    for i in range(n,m+1):
        suma=suma+i
    
    print("la suma de los numeros contenidos en ese rango es: ", suma)