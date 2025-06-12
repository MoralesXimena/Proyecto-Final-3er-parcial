import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


registros = []


def guardar_datos():
    try:
        asistencias = int(asistencias_var.get())
        inasistencias = int(inasistencias_var.get())
        retardos = int(retardos_var.get())
    except ValueError:
        messagebox.showerror("Error", "Asistencias, inasistencias y retardos deben ser números.")
        return

    datos = {
        "Nombre": nombre_var.get(),
        "Fecha Nac.": fecha_nac_var.get(),
        "Tipo Contrato": tipo_contrato_var.get(),
        "Sexo": sexo_var.get(),
        "Grado Estudio": grado_estudio_var.get(),
        "Cédula": cedula_var.get(),
        "Domicilio": domicilio_var.get(),
        "Teléfono": telefono_var.get(),
        "Correo": correo_var.get(),
        "Fecha Ingreso": fecha_ingreso_var.get(),
        "Jornada": jornada_var.get(),
        "Días": dias_var.get(),
        "Asistencias": asistencias,
        "Inasistencias": inasistencias,
        "Retardos": retardos
    }

    if not all(str(valor).strip() for valor in datos.values()):
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return

    registros.append(datos)
    actualizar_historial()
    messagebox.showinfo("Éxito", "Registro guardado correctamente.")
    limpiar_campos()


def actualizar_historial():
    historial.delete(*historial.get_children())
    for i, reg in enumerate(registros, start=1):
        historial.insert("", "end", values=(
            i,
            reg["Nombre"],
            reg["Jornada"],
            reg["Días"],
            reg["Fecha Ingreso"],
            reg["Asistencias"],
            reg["Inasistencias"],
            reg["Retardos"]
        ))


def limpiar_campos():
    for var in [
        nombre_var, fecha_nac_var, tipo_contrato_var, sexo_var, grado_estudio_var,
        cedula_var, domicilio_var, telefono_var, correo_var, fecha_ingreso_var,
        jornada_var, dias_var, asistencias_var, inasistencias_var, retardos_var
    ]:
        var.set("")


ventana = tk.Tk()
ventana.title("Control de Asistencias")
ventana.geometry("1000x650")
ventana.config(bg="lightpink")


nombre_var = tk.StringVar()
fecha_nac_var = tk.StringVar()
tipo_contrato_var = tk.StringVar()
sexo_var = tk.StringVar()
grado_estudio_var = tk.StringVar()
cedula_var = tk.StringVar()
domicilio_var = tk.StringVar()
telefono_var = tk.StringVar()
correo_var = tk.StringVar()
fecha_ingreso_var = tk.StringVar()
jornada_var = tk.StringVar()
dias_var = tk.StringVar()
asistencias_var = tk.StringVar()
inasistencias_var = tk.StringVar()
retardos_var = tk.StringVar()


form_frame = tk.LabelFrame(ventana, text="Registro del trabajador", padx=10, pady=10)
form_frame.pack(fill="x", padx=10, pady=5)

fields = [
    ("Nombre", nombre_var),
    ("Fecha de nacimiento", fecha_nac_var),
    ("Tipo de Contratación", tipo_contrato_var),
    ("Sexo", sexo_var),
    ("Último Grado de Estudio", grado_estudio_var),
    ("Cédula Profesional", cedula_var),
    ("Domicilio", domicilio_var),
    ("Teléfono", telefono_var),
    ("Correo Electrónico", correo_var),
    ("Fecha de ingreso", fecha_ingreso_var)
]

for i, (label_text, var) in enumerate(fields):
    tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="e")
    tk.Entry(form_frame, textvariable=var, width=40).grid(row=i, column=1, pady=2)

tk.Label(form_frame, text="Jornada").grid(row=len(fields), column=0, sticky="e")
jornada_menu = ttk.Combobox(form_frame, textvariable=jornada_var, values=[
    "Matutino (7:00 am-3:00 pm)", "Vespertino (3:00 pm-11:00 pm)", "Nocturno (11:00 pm-7:00 am)"
])
jornada_menu.grid(row=len(fields), column=1, sticky="w", pady=2)

tk.Label(form_frame, text="Días laborales").grid(row=len(fields)+1, column=0, sticky="e")
dias_menu = ttk.Combobox(form_frame, textvariable=dias_var, values=[
    "a: Lunes, Miércoles, Viernes", "b: Martes, Jueves, Sábado"
])
dias_menu.grid(row=len(fields)+1, column=1, sticky="w", pady=2)

tk.Label(form_frame, text="Asistencias").grid(row=len(fields)+2, column=0, sticky="e")
tk.Entry(form_frame, textvariable=asistencias_var, width=10).grid(row=len(fields)+2, column=1, sticky="w", pady=2)

tk.Label(form_frame, text="Inasistencias").grid(row=len(fields)+3, column=0, sticky="e")
tk.Entry(form_frame, textvariable=inasistencias_var, width=10).grid(row=len(fields)+3, column=1, sticky="w", pady=2)

tk.Label(form_frame, text="Retardos").grid(row=len(fields)+4, column=0, sticky="e")
tk.Entry(form_frame, textvariable=retardos_var, width=10).grid(row=len(fields)+4, column=1, sticky="w", pady=2)


tk.Button(ventana, text="Guardar Registro", command=guardar_datos, bg="green", fg="white").pack(pady=10)


historial_frame = tk.LabelFrame(ventana, text="Historial de Trabajadores")
historial_frame.pack(fill="both", expand=True, padx=10, pady=5)

cols = ("#", "Nombre", "Jornada", "Días", "Fecha Ingreso", "Asistencias", "Inasistencias", "Retardos")
historial = ttk.Treeview(historial_frame, columns=cols, show="headings")
for col in cols:
    historial.heading(col, text=col)
    historial.column(col, anchor="center")

historial.pack(fill="both", expand=True)

ventana.mainloop()                       
