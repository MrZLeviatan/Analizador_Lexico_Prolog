# gui.py
# English: GUI for lexical analysis
# Español: Interfaz gráfica para el análisis léxico

import tkinter as tk
from tkinter import ttk
from analizador import analizar_codigo

def analizar():
    texto = entrada_texto.get("1.0", tk.END)
    resultados = analizar_codigo(texto)
    
    tabla.delete(*tabla.get_children())
    for lexema, categoria, pos in resultados:
        tabla.insert("", tk.END, values=(lexema, categoria, pos))

ventana = tk.Tk()
ventana.title("Analizador Léxico - Prolog")

# Área de entrada
entrada_texto = tk.Text(ventana, height=10, width=60)
entrada_texto.pack(pady=10)

# Botón de análisis
btn_analizar = tk.Button(ventana, text="Analizar", command=analizar)
btn_analizar.pack()

# Tabla de resultados
tabla = ttk.Treeview(ventana, columns=("Lexema", "Categoría", "Posición"), show="headings")
tabla.heading("Lexema", text="Lexema")
tabla.heading("Categoría", text="Categoría")
tabla.heading("Posición", text="Posición")
tabla.pack(pady=10)

ventana.mainloop()
