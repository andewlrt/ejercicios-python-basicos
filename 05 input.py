# menu del programa 
print("bienvenido a mini gestor logico ")
print("opciones disponibles")
print("1. AND")
print("2. OR")
print("3.NOT ")
opcion=input("elige una opcion (1/2/3):")
if opcion == "1":
    a=input("ingresa el primer valor logico (true/false):")
    b=input("ingrese el segundo valor logico (true/false):")
    resultado=(a == "true") and (b=="true")
    print(f"Resultado de {a} AND {b} = {resultado}")
elif opcion == "2":
    a = input("Ingresa el primer valor lógico (True/False): ")
    b = input("Ingresa el segundo valor lógico (True/False): ")
    resultado = (a=="true") or (b=="true")
    print(f"resultado de {a} OR {b} = {resultado}")
elif opcion =="3":
    a= input("ingresa un valor logico (true/false):")
    resultado = not (a=="true")
    print(f"resultado de NOT {a}={resultado}")
else:
    print("opcion no valida " )