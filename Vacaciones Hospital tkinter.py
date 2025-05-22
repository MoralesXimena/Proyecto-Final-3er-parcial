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
        tk.Label(self.root, text="Selecciona trabajador:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Selecciona periodo vacacional:").grid(row=1, column=0, padx=10, pady=5)

        self.trabajador_var = tk.StringVar()
        self.trabajador_var.set(self.trabajadores[0]) 

        self.periodo_var = tk.StringVar()
        self.periodo_var.set(self.periodos[0]) 

        trabajador_menu = tk.OptionMenu(self.root, self.trabajador_var, *self.trabajadores)
        trabajador_menu.grid(row=0, column=1, padx=10, pady=5)

        periodo_menu = tk.OptionMenu(self.root, self.periodo_var, *self.periodos)
        periodo_menu.grid(row=1, column=1, padx=10, pady=5)

        boton_registrar = tk.Button(self.root, text="Registrar", command=self.registrar)
        boton_registrar.grid(row=2, column=0, columnspan=2, pady=10)

        lista_label = tk.Label(self.root, text="Elecciones registradas:")
        lista_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.lista_texto = tk.Text(self.root, width=40, height=10, state="disabled")
        self.lista_texto.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def registrar(self):
        trabajador = self.trabajador_var.get()
        periodo = self.periodo_var.get()

        if not trabajador or not periodo:
            messagebox.showerror("Error", "Selecciona un trabajador y un periodo.")
            return

        if trabajador in self.elecciones:
            messagebox.showerror("Error", f"{trabajador} ya ha elegido un periodo.")
            return

        if periodo in self.elecciones.values():
            messagebox.showerror("Error", f"El periodo '{periodo}' ya ha sido seleccionado.")
            return

        self.elecciones[trabajador] = periodo
        messagebox.showinfo("Éxito", f"{trabajador} ha elegido {periodo} como su periodo vacacional.")
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_texto.config(state="normal")
        self.lista_texto.delete(1.0, tk.END)
        for trabajador, periodo in self.elecciones.items():
            self.lista_texto.insert(tk.END, f"{trabajador}: {periodo}\n")
        self.lista_texto.config(state="disabled")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionVacaciones(ventana)

    ventana.mainloop()