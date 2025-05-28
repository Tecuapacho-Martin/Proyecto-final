# Lista para guardar los registros
registros = []

def registrar_persona():
    persona = {}

    persona["nombre"] = input("Ingrese el nombre: ")

    print("Seleccione su turno:")
    print("1. Matutino (06:00 - 14:00)")
    print("2. Vespertino (14:00 - 22:00)")
    print("3. Nocturno (22:00 - 06:00)")
    turno = input("Ingrese una opción (1/2/3): ")

    if turno == "1":
        persona["turno"] = "Matutino"
        persona["entrada"] = "06:00"
        persona["salida"] = "14:00"
    elif turno == "2":
        persona["turno"] = "Vespertino"
        persona["entrada"] = "14:00"
        persona["salida"] = "22:00"
    elif turno == "3":
        persona["turno"] = "Nocturno"
        persona["entrada"] = "22:00"
        persona["salida"] = "06:00"
    else:
        persona["turno"] = "Desconocido"
        persona["entrada"] = "-"
        persona["salida"] = "-"

    print("Seleccione su profesión:")
    print("1. Enfermería")
    print("2. Doctor")
    print("3. Limpieza")
    profesion = input("Ingrese una opción (1/2/3): ")

    if profesion == "1":
        persona["profesion"] = "Enfermería"
    elif profesion == "2":
        persona["profesion"] = "Doctor"
    elif profesion == "3":
        persona["profesion"] = "Limpieza"
    else:
        persona["profesion"] = "No definida"

    persona["faltas"] = int(input("Ingrese número de faltas: "))
    persona["vacaciones"] = int(input("Ingrese número de vacaciones: "))
    persona["asistencias"] = 30 - persona["faltas"] - persona["vacaciones"]

    if persona["faltas"] >= 3:
        persona["estado"] = "Puede faltar"
    else:
        persona["estado"] = "Límite de faltas excedido"

    registros.append(persona)
    print(" Persona registrada con éxito.\n")

def consultar_persona():
    nombre_busqueda = input("Ingrese el nombre que desea consultar: ")
    encontrado = False

    for persona in registros:
        if persona["nombre"].lower() == nombre_busqueda.lower():
            print("----- Registro de", persona["nombre"], "-----")
            print("Profesión:", persona["profesion"])
            print("Turno:", persona["turno"])
            print("Entrada:", persona["entrada"])
            print("Salida:", persona["salida"])
            print("Faltas:", persona["faltas"])
            print("Vacaciones:", persona["vacaciones"])
            print("Asistencias:", persona["asistencias"])
            print("Estado:", persona["estado"])
            print("-----------------------------------\n")
            encontrado = True
            break

    if not encontrado:
        print(" No se encontró a la persona con ese nombre.\n")

def mostrar_menu():
    while True:
        print("===== Sistema de Registro de Asistencia =====")
        print("1. Registrar nueva persona")
        print("2. Consultar persona por nombre")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_persona()
        elif opcion == "2":
            consultar_persona()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")
mostrar_menu()
