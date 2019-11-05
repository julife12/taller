numero=int(input("hola, ponga el numero, pls: "))
nuemero1=numero%1000
nuemero1v2=numero//1000

numero2=nuemero1%100
numero2v2=nuemero1//100

numero3=numero2%10  
numero3v2=numero2//10

n1=numero3*1000
n2=numero3v2*100
n3=numero2v2*10
n4=nuemero1v2*1

nt=n1+n2+n3+n4
print("el inverso del numero es: ",nt)