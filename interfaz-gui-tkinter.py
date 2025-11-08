import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Función que se ejecuta al presionar el botón ---
def simular_envio():
    # 1. Obtener los datos de las variables de Tkinter
    nombre = nombre_var.get()
    email = email_var.get()
    edad = edad_var.get()
    password = password_var.get()

    # 2. Simular el procesamiento de datos
    if not nombre or not email or not password:
        messagebox.showerror("Error de Envío", "Por favor, completa todos los campos requeridos.")
        return

    # 3. Mostrar un mensaje de éxito con los datos
    mensaje = f"¡Formulario enviado con éxito!\n\n"
    mensaje += f"Nombre: {nombre}\n"
    mensaje += f"Email: {email}\n"
    mensaje += f"Edad: {edad} años\n"
    mensaje += f"Contraseña: {'*' * len(password)} (¡Nunca se muestra la real!)"

    messagebox.showinfo("Envío Completo", mensaje)

    # Opcional: Limpiar los campos después del envío
    nombre_var.set("")
    email_var.set("")
    edad_var.set("")
    password_var.set("")

# --- Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("Formulario de Registro Básico")
root.geometry("400x250")
# Añadir relleno a la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# --- Contenedor Principal (Frame) ---
# Usamos un Frame para centrar el formulario y usar Grid de forma limpia
form_frame = ttk.Frame(root, padding="20 20 20 20")
form_frame.grid(row=0, column=0, sticky="nsew")

# Configurar el grid interno para que las columnas se ajusten
for i in range(2):
    form_frame.columnconfigure(i, weight=1)

# --- Variables de Control de Tkinter ---
# Estas variables almacenan el texto de los Entry widgets
nombre_var = tk.StringVar()
email_var = tk.StringVar()
edad_var = tk.StringVar()
password_var = tk.StringVar()

# --- Creación de los Campos (Labels y Entrys) ---

# 1. Campo Nombre
ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
ttk.Entry(form_frame, textvariable=nombre_var, width=30).grid(row=0, column=1, sticky="ew", pady=5, padx=5)

# 2. Campo Email
ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
ttk.Entry(form_frame, textvariable=email_var, width=30).grid(row=1, column=1, sticky="ew", pady=5, padx=5)

# 3. Campo Edad
ttk.Label(form_frame, text="Edad:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
# Usamos tk.Entry ya que ttk no tiene muchas opciones específicas de formato
ttk.Entry(form_frame, textvariable=edad_var, width=30).grid(row=2, column=1, sticky="ew", pady=5, padx=5)

# 4. Campo Contraseña
ttk.Label(form_frame, text="Contraseña:").grid(row=3, column=0, sticky="w", pady=5, padx=5)
# show='*' oculta el texto para contraseñas
ttk.Entry(form_frame, textvariable=password_var, show='*', width=30).grid(row=3, column=1, sticky="ew", pady=5, padx=5)

# --- Botón de Envío ---
# El botón llama a la función simular_envio al ser presionado
ttk.Button(form_frame, text="Enviar Formulario", command=simular_envio).grid(
    row=4, column=0, columnspan=2, pady=20, sticky="ew"
)

# --- Iniciar la Aplicación ---
root.mainloop()

 