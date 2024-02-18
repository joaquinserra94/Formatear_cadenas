x = 10
y = 5
z = x+y
print("Mis numeros son: " + str(x) + " y " + str(y)) #opcion1

print("Mis numeros son {} y {}".format(x,y)) #opcion2
print("La suma de {} y {} es igual a {}".format(x,y,x+y)) #opcion2 operaciones
print("La suma de {} y {} es igual a {}".format(x,y,z)) #opcion2 operaciones con z como variable


#Cadena Literales
color = "rojo"
matricula = 12345

print(f"El auto es {color} y su matricula es {matricula}") #esta ultima es la mas legible
#debemos siempre poner la "f" antes de lo que querramos indicar o frase a decir pero siempre dentro del parentesis
