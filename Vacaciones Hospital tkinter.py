import tkinter as tk
from tkinter import messagebox

class Trabajador:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Trabajador")
        self.root.geometry("400x400")
        self.root.configure(bg="lightpink")

        self.trabajadores = ["Natalia", "Roberto", "Nahomí", "Victor", "Sonia"]
        self.generos = ["Femenino", "Masculino", "Otro"]
        self.areas = ["Administración", "Recursos Humanos", "TI", "Contabilidad", "Logística"]

        self.crear_formulario()

    def crear_formulario(self):
        tk.Label(self.root, text="Selecciona tu nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.nombre_var = tk.StringVar(value=self.trabajadores[0])
        tk.OptionMenu(self.root, self.nombre_var, *self.trabajadores).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Edad:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.edad_entry = tk.Entry(self.root)
        self.edad_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Género:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.genero_var = tk.StringVar(value=self.generos[0])
        tk.OptionMenu(self.root, self.genero_var, *self.generos).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Área de trabajo:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.area_var = tk.StringVar(value=self.areas[0])
        tk.OptionMenu(self.root, self.area_var, *self.areas).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="CURP:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.curp_entry = tk.Entry(self.root)
        self.curp_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.root, text="NSS:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.nss_entry = tk.Entry(self.root)
        self.nss_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Número de Control:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.control_entry = tk.Entry(self.root)
        self.control_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Teléfono:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.telefono_entry = tk.Entry(self.root)
        self.telefono_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Guardar Trabajador", command=self.guardar_trabajador).grid(row=8, column=0, columnspan=2, pady=20)

    def guardar_trabajador(self):
        datos = {
            "Nombre": self.nombre_var.get(),
            "Edad": self.edad_entry.get(),
            "Género": self.genero_var.get(),
            "Área": self.area_var.get(),
            "CURP": self.curp_entry.get(),
            "NSS": self.nss_entry.get(),
            "Control": self.control_entry.get(),
            "Teléfono": self.telefono_entry.get()
        }

        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
            return

        messagebox.showinfo("Éxito", f"Datos del trabajador '{datos['Nombre']}' guardados correctamente.")
        for entry in [self.edad_entry, self.curp_entry, self.nss_entry, self.control_entry, self.telefono_entry]:
            entry.delete(0, tk.END)


class Jornada:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Jornada")
        self.root.geometry("400x400")
        self.root.configure(bg="lightpink")

        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        self.turnos = ["Matutino", "Vespertino", "Nocturno"]

        self.crear_formulario()

    def crear_formulario(self):
        tk.Label(self.root, text="Día de la semana:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.dia_var = tk.StringVar(value=self.dias[0])
        tk.OptionMenu(self.root, self.dia_var, *self.dias).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hora de entrada:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entrada_entry = tk.Entry(self.root)
        self.entrada_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hora de salida:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.salida_entry = tk.Entry(self.root)
        self.salida_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Retardos:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.retardos_entry = tk.Entry(self.root)
        self.retardos_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Asistencia (sí/no):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.asistencia_entry = tk.Entry(self.root)
        self.asistencia_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Faltas:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.faltas_entry = tk.Entry(self.root)
        self.faltas_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Turno:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.turno_var = tk.StringVar(value=self.turnos[0])
        tk.OptionMenu(self.root, self.turno_var, *self.turnos).grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Guardar Jornada", command=self.guardar_jornada).grid(row=7, column=0, columnspan=2, pady=20)

    def guardar_jornada(self):
        datos = {
            "Día": self.dia_var.get(),
            "Entrada": self.entrada_entry.get(),
            "Salida": self.salida_entry.get(),
            "Retardos": self.retardos_entry.get(),
            "Asistencia": self.asistencia_entry.get(),
            "Faltas": self.faltas_entry.get(),
            "Turno": self.turno_var.get()
        }

        if not all(datos.values()):
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
            return

        messagebox.showinfo("Éxito", f"Jornada del día '{datos['Día']}' guardada correctamente.")
        for entry in [self.entrada_entry, self.salida_entry, self.retardos_entry, self.asistencia_entry, self.faltas_entry]:
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root1 = tk.Tk()
    app_trabajador = Trabajador(root1)
    
    root2 = tk.Toplevel()
    app_jornada = Jornada(root2)
    
    root1.mainloop()
