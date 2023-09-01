
opcion = 0

print("zapateria ZAPATICOS")
print(".........")
print("1. agregar producto ala bodega")
print("2. ver productos en bodegas")
print("3. obtener valor del inventario")
print("4. ver productos mas vendidos")
print("5. SALIR")
 
while(opcion !=5):
    opcion = int(input("digita un numero: "))
    
    if(opcion == 1):
        nombre=input("Digita el nombre del producto")
        #agregar datos a una lista
        zapatos.append(nombre)
        print("peluche agregado...")
    elif(opcion == 2):
        print("zapatos")
    elif(opcion == 3):
        print("usted esta en la opcion 3")
    elif(opcion == 4):
        print("usted esta en la opcion 4")
    else:
        print("opcion incorrecta")
print("sali del ciclo")
