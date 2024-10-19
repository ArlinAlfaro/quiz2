import tkinter as tk 
from tkinter import messagebox

# Factor de conversión 
factor_conver = 513.70 #Precio del dolar el 18 de octubre

# Función para hacer la conversión
def conversion():
    try:
        monto_dolar = float(entry_usd.get())
        monto_colones = monto_dolar * factor_conver #Se hace la conversión
        label_resultado.config(text=f"{monto_dolar:.2f} USD = {monto_colones:.2f} CRC", fg="white")
    except ValueError:
        messagebox.showerror("La entrada es inválida", "Ingrese un número que sea válido, por favor.")

# Función para limpiar 
def limpiar():
    entry_usd.delete(0, tk.END)
    label_resultado.config(text="", fg="white")

# Función para salir del programa
def confirmar_salida():
    respuesta = messagebox.askyesno("Salir", "¿Está seguro de que desea salir del programa?")
    if respuesta:
        root.destroy()

# Creación y personalización de la ventana principal

root = tk.Tk()
root.title("Conversor de Moneda de USD a CRC ")
root.geometry("550x300")  # Tamaño de la ventana
root.resizable(False, False)
root.config(bg="#f8bbd0")  #Color

# Se eligió el estilo de fuente y su tamaño
font_titulo = ("Times New Roman", 16, "bold")
font_label = ("Times New Roman", 12)
font_boton = ("Times New Roman", 12, "italic")
font_resultado = ("Times New Roman", 14, "bold italic")

# Ajustes del título
label_titulo = tk.Label(root, text="⋆｡‧˚ʚ Conversor de Dólares (USD) a Colones (CRC) ɞ˚‧｡⋆", font=font_titulo, bg="#f8bbd0", fg="#ff4081")
label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Ajustes del espacio de entrada para USD
label_usd = tk.Label(root, text="Monto en USD:", font=font_label, bg="#f8bbd0", fg="#ff4081")
label_usd.grid(row=1, column=0, padx=10, pady=10)
entry_usd = tk.Entry(root, font=font_label, bg="#fce4ec", fg="#880e4f")
entry_usd.grid(row=1, column=1, padx=10, pady=10)

# Ajustes del botón para hacer la conversión
boton_convertir = tk.Button(root, text="Convertir", font=font_boton, command=conversion, bg="#f48fb1", fg="white")
boton_convertir.grid(row=2, column=0, padx=10, pady=10)

# Ajustes del botón para limpiar
boton_limpiar = tk.Button(root, text="Limpiar", font=font_boton, command=limpiar, bg="#f06292", fg="white")
boton_limpiar.grid(row=2, column=1, padx=10, pady=10)

# Mostrar el resultado
label_resultado = tk.Label(root, text="", font=font_resultado, bg="#f8bbd0", fg="white")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Manejo para la salida con confirmación
root.protocol("WM_DELETE_WINDOW", confirmar_salida)

# Ejecución 
root.mainloop()
