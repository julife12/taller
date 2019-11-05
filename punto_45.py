def funcion_diccionario(x):
    diccionario= {1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
    dia=diccionario[x]
    return dia

a=int(input("digite el numero del dia: "))
print(funcion_diccionario(a))