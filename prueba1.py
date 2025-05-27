import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def es_mayor_de_edad(self):
        return self.edad >= 18

def registrar_trabajador():
    nombre = entry_nombre.get()
    edad_str = entry_edad.get()

    if not nombre or not edad_str.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un nombre y una edad válida.")
        return

    edad = int(edad_str)
    persona = Persona(nombre, edad)

    mensaje_saludo = persona.saludar()
    mensaje_edad = "Es mayor de edad." if persona.es_mayor_de_edad() else "Es menor de edad."

    messagebox.showinfo("Resultado", f"{mensaje_saludo}\n{mensaje_edad}")

ventana = tk.Tk()
ventana.title("Registro de Trabajadores")

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1, column=0, padx=10, pady=10)

entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

boton_registrar = tk.Button(ventana, text="Registrar", command=registrar_trabajador)
boton_registrar.grid(row=2, column=0, columnspan=2, pady=20)

ventana.mainloop()
