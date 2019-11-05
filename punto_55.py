a=int(input("cuantos numeros desea poner? "))
suma=0
for i in range(0,a):
    s=int(input("digite un numero: "))
    suma=suma+s

promedio=suma/a
print("el promedio de los numeros fue: ",promedio)