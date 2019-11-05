s=int(input("digite la cantidad de segundos: "))
h=int((s/60)//60)
print(h)
mi=int(s/60)
print(mi)
s11=s%60
print(s11)
print(h,":",mi,":",s11)