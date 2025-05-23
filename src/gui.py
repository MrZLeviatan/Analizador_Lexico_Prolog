import tkinter as tk                   # Importa el módulo tkinter para crear interfaces gráficas
from tkinter import ttk               # Importa ttk para utilizar widgets más modernos (como Treeview)
from analizador import analizar_codigo  # Importa la función que realiza el análisis léxico

def analizar():
    # Función que se ejecuta al presionar el botón "Analizar"
    
    texto = entrada_texto.get("1.0", tk.END)  # Obtiene el texto completo desde el área de entrada
    resultados = analizar_codigo(texto)       # Analiza el texto con la función importada

    tabla.delete(*tabla.get_children())       # Limpia los resultados anteriores en la tabla

    for lexema, categoria, pos in resultados:
        # Inserta cada resultado del análisis en una nueva fila de la tabla
        tabla.insert("", tk.END, values=(lexema, categoria, pos))

# Configura la ventana principal
ventana = tk.Tk()                            # Crea la ventana principal de la interfaz
ventana.title("Analizador Léxico - Prolog") # Asigna el título de la ventana

# Área de entrada
entrada_texto = tk.Text(ventana, height=10, width=60)  # Crea un área de texto para ingresar el código
entrada_texto.pack(pady=10)                            # Muestra el widget con espacio vertical

# Botón de análisis
btn_analizar = tk.Button(ventana, text="Analizar", command=analizar)  # Crea un botón que ejecuta la función analizar
btn_analizar.pack()                                                    # Muestra el botón en la ventana

# Tabla de resultados
tabla = ttk.Treeview(
    ventana,
    columns=("Lexema", "Categoría", "Posición"),      # Define las columnas de la tabla
    show="headings"                                   # Oculta la columna principal vacía por defecto
)

# Configura los encabezados de las columnas
tabla.heading("Lexema", text="Lexema")               # Encabezado de la columna Lexema
tabla.heading("Categoría", text="Categoría")         # Encabezado de la columna Categoría
tabla.heading("Posición", text="Posición")           # Encabezado de la columna Posición

tabla.pack(pady=10)                                  # Muestra la tabla con espacio vertical

ventana.mainloop()                                   # Inicia el bucle principal de la interfaz gráfica
