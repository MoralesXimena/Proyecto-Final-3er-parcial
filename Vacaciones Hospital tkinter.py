import tkinter as tk
from tkinter import messagebox

class AplicacionVacaciones:
    def __init__(self, root):
        self.trabajadores = ["Natalia", "Roberto", "Nahomí", "Victor", "Sonia"]
        self.periodos = ["Enero-Febrero", "Marzo-Abril", "Mayo-Junio", "Septiembre-Octubre", "Noviembre-Diciembre"]
        self.elecciones = {}

        self.root = root
        self.root.title("Selección de Vacaciones")
        self.root.geometry("500x400")
        self.root.configure(bg="pink")

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Selecciona trabajador:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Selecciona periodo vacacional:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.trabajador_var = tk.StringVar(value=self.trabajadores[0])
        self.periodo_var = tk.StringVar(value=self.periodos[0])

        tk.OptionMenu(self.root, self.trabajador_var, *self.trabajadores).grid(row=0, column=1, padx=10, pady=5)
        tk.OptionMenu(self.root, self.periodo_var, *self.periodos).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Edad:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Área de trabajo:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Label(self.root, text="Hora de entrada:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        self.edad_entry = tk.Entry(self.root)
        self.area_entry = tk.Entry(self.root)
        self.entrada_entry = tk.Entry(self.root)

        self.edad_entry.grid(row=2, column=1, padx=10, pady=5)
        self.area_entry.grid(row=3, column=1, padx=10, pady=5)
        self.entrada_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Button(self.root, text="Registrar", command=self.registrar).grid(row=7, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Datos registrados:").grid(row=8, column=0, columnspan=2, pady=10)

        self.lista_texto = tk.Text(self.root, width=70, height=15, state="disabled")
        self.lista_texto.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    def registrar(self):
        trabajador = self.trabajador_var.get()
        periodo = self.periodo_var.get()
        edad = self.edad_entry.get()
        area = self.area_entry.get()
        entrada = self.entrada_entry.get()

        if not trabajador or not periodo:
            messagebox.showerror("Error", "Selecciona un trabajador y un periodo.")
            return

        if trabajador in self.elecciones:
            messagebox.showerror("Error", f"{trabajador} ya ha registrado sus datos.")
            return

        if periodo in [info['periodo'] for info in self.elecciones.values()]:
            messagebox.showerror("Error", f"El periodo '{periodo}' ya ha sido seleccionado.")
            return

        if not (edad and area and entrada):
            messagebox.showerror("Error", "Todos los campos deben ser completados.")
            return

        self.elecciones[trabajador] = {
            "periodo": periodo,
            "edad": edad,
            "area": area,
            "entrada": entrada,
        }

        messagebox.showinfo("Éxito", f"{trabajador} ha sido registrado correctamente.")
        self.actualizar_lista()
        self.limpiar_campos()

    def actualizar_lista(self):
        self.lista_texto.config(state="normal")
        self.lista_texto.delete(1.0, tk.END)
        for trabajador, info in self.elecciones.items():
            self.lista_texto.insert(tk.END, f"{trabajador}:\n")
            self.lista_texto.insert(tk.END, f"  Periodo: {info['periodo']}\n")
            self.lista_texto.insert(tk.END, f"  Edad: {info['edad']}\n")
            self.lista_texto.insert(tk.END, f"  Área: {info['area']}\n")
            self.lista_texto.insert(tk.END, f"  Entrada: {info['entrada']}\n")
            self.lista_texto.insert(tk.END, "-"*50 + "\n")
        self.lista_texto.config(state="disabled")

    def limpiar_campos(self):
        self.edad_entry.delete(0, tk.END)
        self.area_entry.delete(0, tk.END)
        self.entrada_entry.delete(0, tk.END)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionVacaciones(ventana)
    ventana.mainloop()
