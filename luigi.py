import tkinter as tk
from tkinter import ttk, filedialog

# Función para seleccionar archivo
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        label_archivo.config(text=f"Archivo seleccionado: {archivo}")

# Función para manejar filtros de búsqueda
def aplicar_filtros():
    mes = combo_mes.get()
    anio = combo_anio.get()
    producto = combo_producto.get()
    print(f"Aplicando filtros - Mes: {mes}, Año: {anio}, Producto: {producto}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Gráficos y Filtros")
ventana.geometry("800x600")
ventana.resizable(False, False)

# Banner superior
frame_banner = tk.Frame(ventana, bg="lightblue", height=50)
frame_banner.pack(fill="x")
label_banner = tk.Label(frame_banner, text="BANNER DE EMPRESA", font=("Arial", 16, "bold"), bg="lightblue")
label_banner.pack(pady=10)

# Sección de selección de archivo
frame_archivo = tk.Frame(ventana, pady=10)
frame_archivo.pack(fill="x")
boton_archivo = tk.Button(frame_archivo, text="Seleccionar archivo", command=seleccionar_archivo)
boton_archivo.pack(side="left", padx=20)
label_archivo = tk.Label(frame_archivo, text="No se ha seleccionado ningún archivo", font=("Arial", 10), fg="gray")
label_archivo.pack(side="left", padx=10)

# Sección de filtros de búsqueda
frame_filtros = tk.Frame(ventana, pady=10)
frame_filtros.pack(fill="x")
label_filtros = tk.Label(frame_filtros, text="FILTROS BÚSQUEDA", font=("Arial", 12, "bold"))
label_filtros.grid(row=0, column=0, padx=20, sticky="w")

# Combobox para filtros
# Mes
label_mes = tk.Label(frame_filtros, text="Mes:")
label_mes.grid(row=1, column=0, padx=20, sticky="w")
combo_mes = ttk.Combobox(frame_filtros, values=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                                                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
combo_mes.grid(row=1, column=1, padx=10, pady=5)
combo_mes.set("Seleccionar")

# Año
label_anio = tk.Label(frame_filtros, text="Año:")
label_anio.grid(row=1, column=2, padx=20, sticky="w")
combo_anio = ttk.Combobox(frame_filtros, values=["2020", "2021", "2022", "2023"])
combo_anio.grid(row=1, column=3, padx=10, pady=5)
combo_anio.set("Seleccionar")

# Producto
label_producto = tk.Label(frame_filtros, text="Producto:")
label_producto.grid(row=1, column=4, padx=20, sticky="w")
combo_producto = ttk.Combobox(frame_filtros, values=["Producto 1", "Producto 2", "Producto 3"])
combo_producto.grid(row=1, column=5, padx=10, pady=5)
combo_producto.set("Seleccionar")

# Botón para aplicar filtros
boton_filtros = tk.Button(frame_filtros, text="Aplicar filtros", command=aplicar_filtros)
boton_filtros.grid(row=1, column=6, padx=20, pady=5)

# Sección de gráficos
frame_graficos = tk.Frame(ventana, pady=20)
frame_graficos.pack(fill="x")

# Placeholder para gráfico 1
frame_grafico1 = tk.Frame(frame_graficos, bg="white", width=300, height=200, relief="sunken", borderwidth=1)
frame_grafico1.pack(side="left", padx=20)
label_grafico1 = tk.Label(frame_grafico1, text="Gráfica 1", font=("Arial", 12))
label_grafico1.place(relx=0.5, rely=0.5, anchor="center")

# Placeholder para gráfico 2
frame_grafico2 = tk.Frame(frame_graficos, bg="white", width=300, height=200, relief="sunken", borderwidth=1)
frame_grafico2.pack(side="left", padx=20)
label_grafico2 = tk.Label(frame_grafico2, text="Gráfica 2", font=("Arial", 12))
label_grafico2.place(relx=0.5, rely=0.5, anchor="center")

# Ajustar tamaños fijos para gráficos
frame_grafico1.pack_propagate(False)
frame_grafico2.pack_propagate(False)

# Iniciar la aplicación
ventana.mainloop()
