
pacientes = []


def registrar_paciente(nombre, edad, doctor, camilla):
    paciente = {
        'nombre': nombre,
        'edad': edad,
        'doctor': doctor,
        'camilla': camilla
    }
    pacientes.append(paciente)
    print(f"Paciente {nombre} registrado con éxito.\n")


def contar_pacientes():
    return len(pacientes)
def mostrar_pacientes():
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for i, paciente in enumerate(pacientes, 1):
            print(f"{i}. Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Doctor: {paciente['doctor']}, Camilla: {paciente['camilla']}")
    print()

# Ejemplo de uso
registrar_paciente("Ana Pérez", 35, "Dr. López", 1)
registrar_paciente("Carlos Ruiz", 42, "Dra. Martínez", 2)

print(f"Total de pacientes: {contar_pacientes()}\n")
mostrar_pacientes()
