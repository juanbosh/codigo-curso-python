from pathlib import Path, PureWindowsPath


# La clase Path se convierte en PosixPath o WindowsPath automáticamente
base_dir = Path.home() # La ruta base del usuario (ej: /home/usuario)
nuevo_archivo = base_dir / 'documentos' / 'proyectos' / 'config.ini'

print(nuevo_archivo)
# Salida (ej. en Linux): /home/usuario/documentos/proyectos/config.ini

image_file = base_dir / "downloads" / "midjourney.png"

print(image_file)
print(image_file.root)
print(image_file.suffix)   
print(image_file.name)
print(image_file.stem)
print(image_file.parent)    

q = PureWindowsPath("C:/Users/juan/Documents/python/codigo_python/modulo_pathlib.py")
print(q)
print(q.root) # C:\ deberia imprimir C:\ pero no lo hace
print(q.suffix)   # .py 
print(q.name) # modulo_pathlib.py
print(q.stem)  # modulo_pathlib
print(q.parent) # C:/Users/juan/Documents/python/codigo_python
print(q.parts) # ('C:', 'Users', 'juan', 'Documents', 'python', 'codigo_python', 'modulo_pathlib.py')

cwd = Path.cwd()
archivos = []
for entry in cwd.iterdir():
# Process the entry here
    archivos.append(entry.name)
print(archivos)
