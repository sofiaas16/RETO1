
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
Bievenida = input("Bienvenido al mejor generador de contraseñas")

#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, 
# incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.


Longitud = int(input("¿Cuantos carácteres deseas incluir?: "))
Mayus = int(input("¿Cuantas mayúsculas desea incluir: " ))
Minus = int(input("¿Cuantas minúsculas desea incluir?: "))
Caract = int(input("¿Cuantos caracteres alfanuméricos desea incluir: "))
Simbolos = int(input("¿Cuantos simbolos desea incluir?: "))

contraseña_nueva = True or False 

while (True):
    print ("Se generó la contraseña")
    if {contraseña_nueva} == True:
        print ("Crea otra contraseña: ")
    else: 
        break 

 
