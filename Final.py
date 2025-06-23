
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Trabajador:
    def __init__(self, nombre, ID, puesto, genero, nacimiento, domicilio, telefono, correo):
        self.asistencias = [] 
        self.nombre = nombre
        self.puesto = puesto
        self.ID = ID
        self.genero = genero
        self.nacimiento = nacimiento  # corregido el typo 'nacimineto'
        self.domicilio = domicilio
        self.telefono = telefono
        self.correo = correo
        self.vacaciones = None
        self.turno = None

    def registrar_asistencia(self, fecha_hora):
        self.asistencias.append(fecha_hora)

    def asignar_vacaciones(self, fecha_inicio):
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = inicio + timedelta(days=14)
        self.vacaciones = (inicio, fin)

    def asignar_turno(self, nombre_turno, hora_inicio, hora_fin, dias):
        self.turno = {
            "nombre": nombre_turno,
            "inicio": hora_inicio,
            "fin": hora_fin,
            "dias": dias
        }

    def __str__(self):
        vac_texto = ""
        if self.vacaciones:
            inicio_str = self.vacaciones[0].strftime("%d-%m-%Y")
            fin_str = self.vacaciones[1].strftime("%d-%m-%Y")
            vac_texto = f" | Vacaciones: del {inicio_str} al {fin_str}"
        turno_texto = ""
        if self.turno:
            turno_texto = (f" | Turno: {self.turno['nombre']} "
                           f"{self.turno['inicio']} - {self.turno['fin']} "
                           f"({', '.join(self.turno['dias'])})")
        return f"Nombre: {self.nombre}, ID: {self.ID}, Puesto: {self.puesto}{vac_texto}{turno_texto}"

class RegistroTrabajadores:
    def __init__(self):
        self.trabajadores = []

    def registrar_trabajador(self, nombre, puesto, ID, genero, nacimiento, domicilio, telefono, correo):
        trabajador = Trabajador(nombre, ID, puesto, genero, nacimiento, domicilio, telefono, correo)
        self.trabajadores.append(trabajador)

    def mostrar_trabajadores(self):
        return "\n".join([str(t) for t in self.trabajadores]) if self.trabajadores else "No hay trabajadores registrados."

def registrar_trabajador():
    nombre = entrada_nombre.get()
    puesto = opcion_puesto.get()
    ID = entrada_ID.get()
    genero = opcion_genero.get()
    nacimiento = entrada_nacimiento.get()
    domicilio = entrada_domicilio.get()
    telefono = entrada_telefono.get()
    correo = entrada_correo.get()

    if nombre and puesto and ID:
        registro_trabajadores.registrar_trabajador(nombre, puesto, ID, genero, nacimiento, domicilio, telefono, correo)
        messagebox.showinfo("Éxito", f"Trabajador {nombre} registrado.")
        actualizar_lista_trabajadores()
    else:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

def actualizar_lista_trabajadores():
    global texto_trabajadores
    try:
        texto_trabajadores.config(state=tk.NORMAL)
        texto_trabajadores.delete("1.0", tk.END)
        texto_trabajadores.insert(tk.END, registro_trabajadores.mostrar_trabajadores())
        texto_trabajadores.config(state=tk.DISABLED)
    except:
        pass  # El widget no existe en esta pantalla, así que ignoramos


def interfaz_trabajadores():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Registro de Trabajadores", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre:").pack()
    global entrada_nombre
    entrada_nombre = tk.Entry(area_dinamica)
    entrada_nombre.pack()

    tk.Label(area_dinamica, text="Nacimiento:").pack()
    global entrada_nacimiento
    entrada_nacimiento = tk.Entry(area_dinamica)
    entrada_nacimiento.pack()

    tk.Label(area_dinamica, text="Género:").pack()
    global opcion_genero
    opcion_genero = tk.StringVar()
    opcion_genero.set("Escoge")
    opciones_genero = ["Femenino", "Masculino", "Otro"]
    tk.OptionMenu(area_dinamica, opcion_genero, *opciones_genero).pack()

    tk.Label(area_dinamica, text="Domicilio").pack()
    global entrada_domicilio
    entrada_domicilio = tk.Entry(area_dinamica)
    entrada_domicilio.pack()

    tk.Label(area_dinamica, text="ID:").pack()
    global entrada_ID
    entrada_ID = tk.Entry(area_dinamica)
    entrada_ID.pack()

    tk.Label(area_dinamica, text="Teléfono:").pack()
    global entrada_telefono
    entrada_telefono = tk.Entry(area_dinamica)
    entrada_telefono.pack()

    tk.Label(area_dinamica, text="Correo:").pack()
    global entrada_correo
    entrada_correo = tk.Entry(area_dinamica)
    entrada_correo.pack()

    tk.Label(area_dinamica, text="Puesto:").pack()
    global opcion_puesto
    opcion_puesto = tk.StringVar()
    opcion_puesto.set("Escoge")
    opciones_puesto = ["Doctor", "Enfermero", "Personal"]
    tk.OptionMenu(area_dinamica, opcion_puesto, *opciones_puesto).pack()

    tk.Button(area_dinamica, text="Registrar Trabajador", command=registrar_trabajador).pack(pady=10)

    global texto_trabajadores
    texto_trabajadores = tk.Text(area_dinamica, height=10, width=50)
    texto_trabajadores.pack()
    texto_trabajadores.config(state=tk.DISABLED)
    actualizar_lista_trabajadores()

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


def interfaz_turnos():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Asignación de Turno y Horario", font=("Arial", 14)).pack(pady=10)

    if not registro_trabajadores.trabajadores:
        tk.Label(area_dinamica, text="No hay trabajadores registrados.").pack()
        return

    tk.Label(area_dinamica, text="Selecciona un trabajador:").pack()
    global trabajador_turno
    trabajador_turno = tk.StringVar()
    trabajador_turno.set(registro_trabajadores.trabajadores[0].nombre)
    tk.OptionMenu(area_dinamica, trabajador_turno, *[t.nombre for t in registro_trabajadores.trabajadores]).pack()

    tk.Label(area_dinamica, text="Nombre del Turno:").pack()
    global entrada_turno
    entrada_turno = tk.Entry(area_dinamica)
    entrada_turno.pack()

    tk.Label(area_dinamica, text="Hora de Inicio (HH:MM):").pack()
    global entrada_inicio
    entrada_inicio = tk.Entry(area_dinamica)
    entrada_inicio.pack()

    tk.Label(area_dinamica, text="Hora de Fin (HH:MM):").pack()
    global entrada_fin
    entrada_fin = tk.Entry(area_dinamica)
    entrada_fin.pack()

    tk.Label(area_dinamica, text="Días Laborales:").pack()
    global dias_vars
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    dias_vars = {}
    for dia in dias:
        var = tk.BooleanVar()
        tk.Checkbutton(area_dinamica, text=dia, variable=var).pack(anchor="w")
        dias_vars[dia] = var

    tk.Button(area_dinamica, text="Asignar Turno", command=asignar_turno).pack(pady=10)

def asignar_turno():
    nombre = trabajador_turno.get()
    nombre_turno = entrada_turno.get()
    inicio = entrada_inicio.get()
    fin = entrada_fin.get()
    dias = [dia for dia, var in dias_vars.items() if var.get()]

    if not (nombre_turno and inicio and fin and dias):
        messagebox.showerror("Error", "Completa todos los campos y selecciona al menos un día.")
        return

    for t in registro_trabajadores.trabajadores:
        if t.nombre == nombre:
            t.asignar_turno(nombre_turno, inicio, fin, dias)
            messagebox.showinfo("Éxito", f"Turno asignado a {nombre}.")
            actualizar_lista_trabajadores()
            break
def interfaz_asistencia():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Registro de Asistencia", font=("Arial", 14)).pack(pady=10)

    nombres = [t.nombre for t in registro_trabajadores.trabajadores]
    if not nombres:
        tk.Label(area_dinamica, text="No hay trabajadores registrados.").pack()
        return

    global entrada_nombre_asistencia
    tk.Label(area_dinamica, text="Nombre del trabajador:").pack()
    entrada_nombre_asistencia = tk.StringVar()
    entrada_nombre_asistencia.set(nombres[0])
    tk.OptionMenu(area_dinamica, entrada_nombre_asistencia, *nombres).pack()

    tk.Button(area_dinamica, text="Registrar Asistencia", command=registrar_asistencia_por_nombre).pack(pady=10)

def obtener_trabajador_por_nombre(nombre):
    for t in registro_trabajadores.trabajadores:
        if t.nombre == nombre:
            return t
    return None

def registrar_asistencia_por_nombre():
    nombre = entrada_nombre_asistencia.get()
    trabajador = obtener_trabajador_por_nombre(nombre)

    if not trabajador:
        messagebox.showerror("Error", "Trabajador no encontrado.")
        return

    if not trabajador.turno:
        messagebox.showerror("Turno no asignado", "El trabajador no tiene turno y horario asignados.")
        return

    ahora = datetime.now().strftime("%H:%M")
    turno = trabajador.turno
    dias = turno["dias"]

    hoy = datetime.now().strftime("%A")  # Día en inglés (e.g. "Monday")
    mapa_dias = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    dia_actual = mapa_dias.get(hoy, "")
    if dia_actual not in dias:
        messagebox.showerror("Fuera de turno", f"Hoy ({dia_actual}) no está dentro de los días laborales asignados.")
        return

    messagebox.showinfo("Asistencia registrada", f"Asistencia registrada para {nombre} a las {ahora}.")
    trabajador.registrar_asistencia(datetime.now().strftime("%Y-%m-%d %H:%M"))
def interfaz_historial():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Historial de Asistencias", font=("Arial", 14)).pack(pady=10)

    nombres = [t.nombre for t in registro_trabajadores.trabajadores]
    if not nombres:
        tk.Label(area_dinamica, text="No hay trabajadores registrados.").pack()
        return

    global seleccion_historial
    tk.Label(area_dinamica, text="Selecciona un trabajador:").pack()
    seleccion_historial = tk.StringVar()
    seleccion_historial.set(nombres[0])
    tk.OptionMenu(area_dinamica, seleccion_historial, *nombres).pack()

    tk.Button(area_dinamica, text="Mostrar historial", command=mostrar_historial_asistencia).pack(pady=10)

    global texto_historial
    texto_historial = tk.Text(area_dinamica, height=10, width=50)
    texto_historial.pack()
    texto_historial.config(state=tk.DISABLED)

def mostrar_historial_asistencia():
    nombre = seleccion_historial.get()
    trabajador = obtener_trabajador_por_nombre(nombre)

    texto_historial.config(state=tk.NORMAL)
    texto_historial.delete("1.0", tk.END)

    if trabajador.asistencias:
        for entrada in trabajador.asistencias:
            texto_historial.insert(tk.END, f"{entrada}\n")
    else:
        texto_historial.insert(tk.END, "Sin registros de asistencia.")

    texto_historial.config(state=tk.DISABLED)


def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

registro_trabajadores = RegistroTrabajadores()
ventana_principal = tk.Tk()
ventana_principal.title("Gestión de Hospital")
ventana_principal.geometry("700x700")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Trabajadores", command=interfaz_trabajadores, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Vacaciones", command=interfaz_vacaciones, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Turnos", command=interfaz_turnos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Historial", command=interfaz_historial, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Asistencia", command=interfaz_asistencia, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)



interfaz_trabajadores()
ventana_principal.mainloop()
