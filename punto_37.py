dc=int(input("cuanto es la distancia a recorrer?"))
dias=int(input("cuantos dias se va a quedar?"))
precio=dc*5000

if precio<100000:
    precio=100000

if dc>1000 and dias>7:
    precio=precio*0.85

print("el precio total de su viaje es: ", precio)