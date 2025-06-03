class Paciente:
    def __init__(self, nombre, edad, doctor, camilla):
        self.nombre = nombre
        self.edad = edad
        self.doctor = doctor
        self.camilla = camilla

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Doctor: {self.doctor}, Camilla: {self.camilla}"

class Hospital:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self):
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        doctor = input("Doctor asignado: ")
        camilla = int(input("Número de camilla: "))
        paciente = Paciente(nombre, edad, doctor, camilla)
        self.pacientes.append(paciente)
        print("Paciente registrado con éxito.\n")

    def contar_pacientes(self):
        print(f"Total de pacientes en el hospital: {len(self.pacientes)}\n")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.\n")
        else:
            for i, p in enumerate(self.pacientes, 1):
                print(f"{i}. {p}")
            print()

    def menu(self):
        while True:
            print("----- HOSPITAL - MENÚ -----")
            print("1. Registrar paciente")
            print("2. Ver cantidad de pacientes")
            print("3. Mostrar lista de pacientes")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                self.registrar_paciente()
            elif opcion == '2':
                self.contar_pacientes()
            elif opcion == '3':
                self.mostrar_pacientes()
            elif opcion == '4':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intenta de nuevo.\n")

# Crear hospital e iniciar menú
hospital = Hospital()
hospital.menu()
