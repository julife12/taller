a=int(input("cuantos numeros desea poner? "))
suma1=0
suma2=0
contador1=0
contador2=0
for i in range(0,a):
    s=int(input("digite un numero: "))
    if s%2==0:
        suma1=suma1+s
        contador1=contador1+1
    else:
        suma2=suma2+s
        contador2=contador2+1

promedio1=suma1/contador1
promedio2=suma2/contador2
print("el promedio de los numeros pares fue: ",promedio1, " y de los impares fue: ", promedio2)