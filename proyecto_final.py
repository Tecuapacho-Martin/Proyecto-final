import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Trabajador:
    def _init_(self, nombre, ID, puesto):
        self.nombre = nombre
        self.puesto = puesto
        self.ID = ID
        self.vacaciones = None  

    def asignar_vacaciones(self, fecha_inicio):
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = inicio + timedelta(days=14) 
        self.vacaciones = (inicio, fin)

    def _str_(self):
        vac_texto = ""
        if self.vacaciones:
            inicio_str = self.vacaciones[0].strftime("%d-%m-%Y")
            fin_str = self.vacaciones[1].strftime("%d-%m-%Y")
            vac_texto = f" | Vacaciones: del {inicio_str} al {fin_str}"
        return f"Nombre: {self.nombre}, ID: {self.ID}, Puesto: {self.puesto}{vac_texto}"

class RegistroTrabajadores:
    def _init_(self):
        self.trabajadores = []

    # Método corregido: recibe parámetros para crear un trabajador
    def registrar_trabajador(self, nombre, puesto, ID):
        trabajador = Trabajador(nombre, ID, puesto)
        self.trabajadores.append(trabajador)

    def mostrar_trabajadores(self):
        return "\n".join([str(t) for t in self.trabajadores]) if self.trabajadores else "No hay trabajadores registrados."

class Paciente:
    def _init_(self, nombre, edad, doctor, camilla):
        self.nombre = nombre
        self.edad = edad
        self.doctor = doctor
        self.camilla = camilla

    def _str_(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Doctor: {self.doctor}, Camilla: {self.camilla}"

class RegistroPacientes:
    def _init_(self):
        self.pacientes = []

    def registrar_paciente(self, nombre, edad, doctor, camilla):
        paciente = Paciente(nombre, edad, doctor, camilla)
        self.pacientes.append(paciente)

    def mostrar_pacientes(self):
        return "\n".join([str(p) for p in self.pacientes]) if self.pacientes else "No hay pacientes registrados."

# Función para registrar trabajador, llama al método de RegistroTrabajadores
def registrar_trabajador():
    nombre = entry_nombre_trabajador.get()
    puesto = opcion_puesto.get()
    ID = entry_ID_trabajador.get()

    if nombre and puesto and ID:
        registro_trabajadores.registrar_trabajador(nombre, puesto, ID)
        messagebox.showinfo("Éxito", f"Trabajador {nombre} registrado.")
        actualizar_lista_trabajadores()
    else:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

def actualizar_lista_trabajadores():
    text_trabajadores.config(state=tk.NORMAL)
    text_trabajadores.delete("1.0", tk.END)
    text_trabajadores.insert(tk.END, registro_trabajadores.mostrar_trabajadores())
    text_trabajadores.config(state=tk.DISABLED)

def registrar_paciente():
    nombre = entry_nombre_paciente.get()
    edad = entry_edad.get()
    doctor = entry_doctor.get()
    camilla = entry_camilla.get()
    
    if nombre and edad.isdigit() and doctor and camilla.isdigit():
        registro_pacientes.registrar_paciente(nombre, int(edad), doctor, int(camilla))
        messagebox.showinfo("Éxito", f"Paciente {nombre} registrado con éxito.")
        actualizar_lista_pacientes()
    else:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

def actualizar_lista_pacientes():
    text_pacientes.config(state=tk.NORMAL)
    text_pacientes.delete("1.0", tk.END)
    text_pacientes.insert(tk.END, registro_pacientes.mostrar_pacientes())
    text_pacientes.config(state=tk.DISABLED)

def interfaz_trabajadores():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Registro de Trabajadores", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(area_dinamica, text="Nombre:").pack()
    global entry_nombre_trabajador
    entry_nombre_trabajador = tk.Entry(area_dinamica)
    entry_nombre_trabajador.pack()

    tk.Label(area_dinamica, text="ID:").pack()
    global entry_ID_trabajador
    entry_ID_trabajador = tk.Entry(area_dinamica)
    entry_ID_trabajador.pack()

    tk.Label(area_dinamica, text="Puesto:").pack()
    global opcion_puesto
    opcion_puesto = tk.StringVar()
    opcion_puesto.set("Doctor")  
    opciones = ["Doctor", "Enfermero", "Personal"]
    tk.OptionMenu(area_dinamica, opcion_puesto, *opciones).pack()

    tk.Button(area_dinamica, text="Registrar Trabajador", command=registrar_trabajador).pack(pady=10)
    
    global text_trabajadores
    text_trabajadores = tk.Text(area_dinamica, height=10, width=50)
    text_trabajadores.pack()
    text_trabajadores.config(state=tk.DISABLED)
    actualizar_lista_trabajadores()

def interfaz_pacientes():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Registro de Pacientes", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(area_dinamica, text="Nombre:").pack()
    global entry_nombre_paciente
    entry_nombre_paciente = tk.Entry(area_dinamica)
    entry_nombre_paciente.pack()

    tk.Label(area_dinamica, text="Edad:").pack()
    global entry_edad
    entry_edad = tk.Entry(area_dinamica)
    entry_edad.pack()

    tk.Label(area_dinamica, text="Doctor:").pack()
    global entry_doctor
    entry_doctor = tk.Entry(area_dinamica)
    entry_doctor.pack()

    tk.Label(area_dinamica, text="Camilla:").pack()
    global entry_camilla
    entry_camilla = tk.Entry(area_dinamica)
    entry_camilla.pack()

    tk.Button(area_dinamica, text="Registrar Paciente", command=registrar_paciente).pack(pady=10)
    
    global text_pacientes
    text_pacientes = tk.Text(area_dinamica, height=10, width=50)
    text_pacientes.pack()
    text_pacientes.config(state=tk.DISABLED)
    actualizar_lista_pacientes()
    
def interfaz_vacaciones():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Asignar Vacaciones", font=("Arial", 14)).pack(pady=10)
    nombres = [t.nombre for t in registro_trabajadores.trabajadores]
    if not nombres:
        tk.Label(area_dinamica, text="No hay trabajadores registrados.").pack()
        return

    tk.Label(area_dinamica, text="Selecciona un trabajador:").pack()
    global seleccion_trabajador
    seleccion_trabajador = tk.StringVar()
    seleccion_trabajador.set(nombres[0])
    tk.OptionMenu(area_dinamica, seleccion_trabajador, *nombres).pack()

    tk.Label(area_dinamica, text="Fecha de inicio (AAAA-MM-DD):").pack()
    global entry_fecha_inicio
    entry_fecha_inicio = tk.Entry(area_dinamica)
    entry_fecha_inicio.pack()

    tk.Button(area_dinamica, text="Asignar Vacaciones", command=asignar_vacaciones).pack(pady=10)

    global text_vacaciones
    text_vacaciones = tk.Text(area_dinamica, height=10, width=50)
    text_vacaciones.pack()
    text_vacaciones.config(state=tk.DISABLED)
    actualizar_lista_trabajadores()  

def asignar_vacaciones():
    nombre = seleccion_trabajador.get()
    fecha_inicio = entry_fecha_inicio.get()
    try:
        datetime.strptime(fecha_inicio, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Usa AAAA-MM-DD.")
        return
    for t in registro_trabajadores.trabajadores:
        if t.nombre == nombre:
            if t.vacaciones:
                respuesta = messagebox.askyesno(
                    "Confirmar",
                    f"El trabajador {nombre} ya tiene vacaciones asignadas del "
                    f"{t.vacaciones[0].strftime('%d-%m-%Y')} al {t.vacaciones[1].strftime('%d-%m-%Y')}.\n"
                    "¿Deseas sobrescribirlas?"
                )
                if not respuesta:
                    return
            t.asignar_vacaciones(fecha_inicio)
            messagebox.showinfo("Éxito", f"Vacaciones asignadas a {nombre}.")
            actualizar_lista_trabajadores()
            break

def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

registro_trabajadores = RegistroTrabajadores()
registro_pacientes = RegistroPacientes()

ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Hospital")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Trabajadores", command=interfaz_trabajadores, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Pacientes", command=interfaz_pacientes, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Vacaciones", command=interfaz_vacaciones, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

interfaz_trabajadores()
ventana_principal.mainloop()
