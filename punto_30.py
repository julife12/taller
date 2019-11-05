v1=int(input("digite el valor del producto: "))
valori=v1*0.19
vf=v1+valori
if vf>150000:
    vf-=(vf*0.05)
    print("el valor del producto final es: ",vf)
else:
    print("el valor final del producto es: ", vf)