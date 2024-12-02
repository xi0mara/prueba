





# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image, ImageTk  # Para manejar imágenes
# import pandas as pd

# # Función para cargar el archivo Excel
# def cargar_archivo():
#     global datos
#     archivo = filedialog.askopenfilename(
#         title="Seleccionar archivo Excel",
#         filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
#     )
#     if archivo:
#         try:
#             datos = pd.read_excel(archivo)  # Cargar datos del archivo
#             messagebox.showinfo("Éxito", "Archivo cargado correctamente")
#             boton_mostrar.config(state=tk.NORMAL)  # Habilitar el botón de mostrar alumnos
#         except Exception as e:
#             messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

# # Función para mostrar alumnos de una sección
# def mostrar_alumnos():
#     if datos is not None:
#         seccion = entry_seccion.get().strip().upper()
#         if seccion:
#             alumnos_seccion = datos[datos['SECCIÓN'] == seccion]
#             if not alumnos_seccion.empty:
#                 nombres = "\n".join(alumnos_seccion['NOMBRE'].tolist())
#                 messagebox.showinfo(f"Alumnos de la sección {seccion}", nombres)
#             else:
#                 messagebox.showinfo("Sin resultados", f"No se encontraron alumnos en la sección {seccion}.")
#         else:
#             messagebox.showerror("Error", "Por favor, ingrese una sección.")
#     else:
#         messagebox.showerror("Error", "Por favor, cargue primero un archivo Excel.")

# # Configuración inicial
# ventana = tk.Tk()
# ventana.title("Gestión de Alumnos")
# ventana.geometry("500x400")

# # Variable para almacenar los datos
# datos = None

# # Agregar logo
# try:
#     imagen = Image.open("logo_uni.png")  # Cambia "logo.png" por el nombre de tu imagen
#     imagen = imagen.resize((100, 100), Image.ANTIALIAS)  # Redimensionar si es necesario
#     logo = ImageTk.PhotoImage(imagen)
#     label_logo = tk.Label(ventana, image=logo)
#     label_logo.place(x=20, y=20)  # Posicionar el logo en la parte superior izquierda
# except Exception as e:
#     print(f"Error al cargar el logo: {e}")

# # Etiqueta de bienvenida
# label_bienvenida = tk.Label(ventana, text="HOLA BIENVENIDOS ALUMNOS DE LA SECCIÓN", font=("Arial", 12))
# label_bienvenida.place(x=150, y=50)

# # Campo de entrada para la sección
# entry_seccion = tk.Entry(ventana, width=5, font=("Arial", 12))
# entry_seccion.place(x=420, y=50)

# # Botón para cargar archivo
# boton_cargar = tk.Button(ventana, text="Cargar archivo Excel", command=cargar_archivo, font=("Arial", 10, "bold"), bg="blue", fg="white")
# boton_cargar.place(x=180, y=100)

# # Botón para mostrar alumnos
# boton_mostrar = tk.Button(ventana, text="MOSTRAR ALUMNOS", command=mostrar_alumnos, font=("Arial", 10, "bold"), bg="red", fg="white", state=tk.DISABLED)
# boton_mostrar.place(x=180, y=150)

# # Ejecutar la aplicación
# ventana.mainloop()

# *******************************************************************************
# import tkinter as tk
# from tkinter import Menu, Frame, Label, Text, Scrollbar, filedialog
# from PIL import Image, ImageTk

# # Crear ventana principal
# ventana = tk.Tk()
# ventana.title("ALUMNOS")
# ventana.geometry("800x600")

# # Función para cargar una imagen (placeholder para funcionalidad)
# def cargar_imagen():
#     archivo = filedialog.askopenfilename(
#         title="Seleccionar imagen",
#         filetypes=(("Archivos de imagen", "*.png;*.jpg;*.jpeg"), ("Todos los archivos", "*.*"))
#     )
#     if archivo:
#         # Aquí puedes manejar la carga de la imagen o realizar análisis
#         print(f"Imagen cargada: {archivo}")

# # Crear barra de menús
# menu_bar = Menu(ventana)
# ventana.config(menu=menu_bar)

# # Menús desplegables
# menu_archivo = Menu(menu_bar, tearoff=0)
# menu_archivo.add_command(label="Abrir", command=cargar_imagen)
# menu_archivo.add_separator()
# menu_archivo.add_command(label="Salir", command=ventana.quit)
# menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

# menu_configurar = Menu(menu_bar, tearoff=0)
# menu_configurar.add_command(label="Preferencias")
# menu_bar.add_cascade(label="Configurar", menu=menu_configurar)

# menu_ayuda = Menu(menu_bar, tearoff=0)
# menu_ayuda.add_command(label="Acerca de")
# menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# # Crear secciones de la interfaz
# # Sección de información del paciente
# frame_info = Frame(ventana, borderwidth=2, relief="groove")
# frame_info.place(x=10, y=10, width=250, height=200)
# label_info = Label(frame_info, text="Información del Paciente:", font=("Arial", 10, "bold"))
# label_info.pack(anchor="nw", padx=10, pady=5)
# info_text = Text(frame_info, wrap="word", height=8, width=30)
# info_text.insert("1.0", "Código: 123456\nDNI: 10203040\nNombres: Samuel Harris\nApellidos: Altman\nEdad: 40\nCiudad: Lima\nGénero: Masculino")
# info_text.config(state="disabled")  # Hacerlo de solo lectura
# info_text.pack(padx=10, pady=5)

# # Sección de lista de imágenes
# frame_lista = Frame(ventana, borderwidth=2, relief="groove")
# frame_lista.place(x=10, y=220, width=250, height=250)
# label_lista = Label(frame_lista, text="Lista de Imágenes", font=("Arial", 10, "bold"))
# label_lista.pack(anchor="nw", padx=10, pady=5)

# # Placeholder para una imagen (puedes cargar una imagen real)
# placeholder_img = Image.new("RGB", (200, 150), color="gray")
# img_tk = ImageTk.PhotoImage(placeholder_img)
# label_imagen = Label(frame_lista, image=img_tk)
# label_imagen.pack(padx=10, pady=5)

# # Sección de visualización
# frame_visualizar = Frame(ventana, borderwidth=2, relief="groove")
# frame_visualizar.place(x=270, y=10, width=400, height=460)
# label_visualizar = Label(frame_visualizar, text="Visualizar", font=("Arial", 10, "bold"))
# label_visualizar.pack(anchor="nw", padx=10, pady=5)

# # Placeholder para el área de visualización (puedes cargar imágenes o gráficos aquí)
# canvas_visualizar = Label(frame_visualizar, bg="black", width=50, height=20)
# canvas_visualizar.pack(padx=10, pady=5)

# # Sección de resultados
# frame_resultados = Frame(ventana, borderwidth=2, relief="groove")
# frame_resultados.place(x=680, y=10, width=100, height=460)
# label_resultados = Label(frame_resultados, text="Resultados", font=("Arial", 10, "bold"))
# label_resultados.pack(anchor="nw", padx=10, pady=5)

# # Área de texto con barra de desplazamiento
# scrollbar = Scrollbar(frame_resultados)
# scrollbar.pack(side="right", fill="y")
# text_resultados = Text(frame_resultados, wrap="word", yscrollcommand=scrollbar.set, width=12, height=25)
# text_resultados.insert("1.0", "Resultados aparecerán aquí...")
# text_resultados.config(state="disabled")  # Solo lectura
# text_resultados.pack(side="left", fill="both", padx=5, pady=5)
# scrollbar.config(command=text_resultados.yview)

# # Iniciar la aplicación
# ventana.mainloop()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import tkinter as tk
from tkinter import Menu, Frame, Label, Text, Scrollbar, filedialog, simpledialog
from PIL import Image, ImageTk

# Función para agregar un nuevo alumno
def agregar_alumno():
    global info_text
    # Solicitar información del alumno
    codigo = simpledialog.askstring("Nuevo Alumno", "Ingrese el código del alumno:")
    dni = simpledialog.askstring("Nuevo Alumno", "Ingrese el DNI del alumno:")
    nombres = simpledialog.askstring("Nuevo Alumno", "Ingrese los nombres del alumno:")
    apellidos = simpledialog.askstring("Nuevo Alumno", "Ingrese los apellidos del alumno:")
    edad = simpledialog.askinteger("Nuevo Alumno", "Ingrese la edad del alumno:")
    ciudad = simpledialog.askstring("Nuevo Alumno", "Ingrese la ciudad del alumno:")
    genero = simpledialog.askstring("Nuevo Alumno", "Ingrese el género del alumno (Masculino/Femenino):")

    # Actualizar la información en la sección "Información del Alumno"
    alumno_info = (
        f"Código: {codigo}\n"
        f"DNI: {dni}\n"
        f"Nombres: {nombres}\n"
        f"Apellidos: {apellidos}\n"
        f"Edad: {edad}\n"
        f"Ciudad: {ciudad}\n"
        f"Género: {genero}"
    )
    info_text.config(state="normal")  # Habilitar edición
    info_text.delete("1.0", "end")  # Limpiar información anterior
    info_text.insert("1.0", alumno_info)
    info_text.config(state="disabled")  # Volver a deshabilitar edición


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Alumnos")
ventana.geometry("800x600")

# Crear barra de menús
menu_bar = Menu(ventana)
ventana.config(menu=menu_bar)

# Menú "Archivo" con opción "Nuevo"
menu_archivo = Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=agregar_alumno)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

menu_configurar = Menu(menu_bar, tearoff=0)
menu_configurar.add_command(label="Preferencias")
menu_bar.add_cascade(label="Configurar", menu=menu_configurar)

menu_ayuda = Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Acerca de")
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Sección de información del alumno
frame_info = Frame(ventana, borderwidth=2, relief="groove")
frame_info.place(x=10, y=10, width=250, height=200)
label_info = Label(frame_info, text="Información del Alumno:", font=("Arial", 10, "bold"))
label_info.pack(anchor="nw", padx=10, pady=5)
info_text = Text(frame_info, wrap="word", height=8, width=30)
info_text.insert("1.0", "Ingrese un nuevo alumno desde el menú 'Archivo > Nuevo'.")
info_text.config(state="disabled")  # Hacerlo de solo lectura
info_text.pack(padx=10, pady=5)

# Sección de lista de imágenes
frame_lista = Frame(ventana, borderwidth=2, relief="groove")
frame_lista.place(x=10, y=220, width=250, height=250)
label_lista = Label(frame_lista, text="Lista de Imágenes", font=("Arial", 10, "bold"))
label_lista.pack(anchor="nw", padx=10, pady=5)

# Mostrar el logo en la lista de imágenes
try:
    ruta_logo = r"C:\Users\XIOMARA\Desktop\TESTING\logo.png"  # Ruta completa
    imagen_logo = Image.open(ruta_logo)
    imagen_logo = imagen_logo.resize((200, 150), Image.Resampling.LANCZOS)  # Corregido
    logo_img = ImageTk.PhotoImage(imagen_logo)
    label_logo = Label(frame_lista, image=logo_img)
    label_logo.pack(padx=10, pady=5)
except Exception as e:
    print(f"Error al cargar el logo: {e}")

# Sección de visualización
frame_visualizar = Frame(ventana, borderwidth=2, relief="groove")
frame_visualizar.place(x=270, y=10, width=400, height=460)
label_visualizar = Label(frame_visualizar, text="Visualizar", font=("Arial", 10, "bold"))
label_visualizar.pack(anchor="nw", padx=10, pady=5)

# Placeholder para el área de visualización (puedes cargar imágenes o gráficos aquí)
canvas_visualizar = Label(frame_visualizar, bg="black", width=50, height=20)
canvas_visualizar.pack(padx=10, pady=5)

# Sección de resultados
frame_resultados = Frame(ventana, borderwidth=2, relief="groove")
frame_resultados.place(x=680, y=10, width=100, height=460)
label_resultados = Label(frame_resultados, text="Resultados", font=("Arial", 10, "bold"))
label_resultados.pack(anchor="nw", padx=10, pady=5)

# Área de texto con barra de desplazamiento
scrollbar = Scrollbar(frame_resultados)
scrollbar.pack(side="right", fill="y")
text_resultados = Text(frame_resultados, wrap="word", yscrollcommand=scrollbar.set, width=12, height=25)
text_resultados.insert("1.0", "Resultados aparecerán aquí...")
text_resultados.config(state="disabled")  # Solo lectura
text_resultados.pack(side="left", fill="both", padx=5, pady=5)
scrollbar.config(command=text_resultados.yview)

# Iniciar la aplicación
ventana.mainloop()
