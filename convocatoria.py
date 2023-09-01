# 0.salir
# 1.ingresar gente
# 2.ver quien se apuntaron 
# 3.ver quien pago
# 4.ver quien no
# 5.cambiar info
# 6.retirarse

print("...Fiesta Mundial...")
print(".......")
print("1. REGISTRAR INVITADO")
print("2. VER LISTA INVITADOS")
print("3. VER INVITADOS VIP")
print("4. COBRANZA")
print("5. EDITAR INFORMACION")
print("6. RETIRAR INVITADOS")
print("7. ...........")

opcion=90
usuarios=[]

while(opcion != 0):
    invitado={}
    
    opcion = int(input("Digita una opcion: "))
    if opcion==1:
        invitado["nombre"]=input("ingrese su nombre: ")
        invitado["id"]=int(input("ingrese su id: "))
        invitado["cedula"]=input("ingrese su cedula: ")
        invitado["eps"]=input("ingrese su EPS: ")
        invitado["estado"]=bool(input("Ya pago?: "))
        invitado["valorcuota"]=float(input("ingrese la cuota: "))
        invitado["edad"]=int(input("ingrese su edad: "))
        
        usuario.append(invitado)
        
    elif opcion==2:
        #recorriendo una lista        
        for persona in usuarios:
            print(f"persona:{persona['nombre']}")
            print(f"persona:{persona['id']}")
            print(f"persona:{persona['cedula']}")
            print(f"persona:{persona['eps']}")
            print(f"persona:{persona['estado']}")
            print(f"persona:{persona['valorcuota']}")
            print(f"persona:{persona['edad']}") 
    elif opcion==3:
        for persona in usuarios:
            if persona["estado"]==True:
                print(persona)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("opcion invalida")
        
    
            