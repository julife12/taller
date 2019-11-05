a=int(input("cuantos numeros desea poner? "))
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0

for i in range(0,a):
    s=int(input("digite un numero: "))
    if s>=0:
        contador1=contador1+1
    else: 
        contador2=contador2+1

    if s%2==0:
        contador3=contador3+1
    else:
        contador4=contador4+1
    
    if s%8==0:
        contador5=contador5+1

print("hubo ", contador1, " positivos. ", contador2, " negativos. ", contador3, " pares. ", contador4, "impares y ", contador5, " multiplos de 8")