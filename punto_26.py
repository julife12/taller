print("a=True or False\n"+"b=False or False\n"+"c= True and True\n"+"d=False and True\n"
        +"e=(false and true) or (true and true)\n"+"f=(false or false) and (true and true)")
p= input("cual de las siguientes expresiones quiere saber: ")
if p=="a":
    print(True or False)
elif p=="b":
    print(False or False)
elif p=="c":
    print(True and True)
elif p=="d":
    print(False and True)
elif p=="e":
    print((False and True) or (True and True))
elif p=="f":
    print((False or False) and (True and True))
