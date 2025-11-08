from enum import Enum

# 1. Definimos los estados con valores explícitos
class Estado(Enum):
    PREPARANDO = 1
    EN_TRANSITO = 2
    EN_REPARTO = 3
    ENTREGADO = 4
    INCIDENCIA = 5

# 2. Clase Paquete

class Paquete:
    def __init__(self, id: str, estado: Estado = Estado.PREPARANDO):
        self.id = id
        self.estado = estado

    # Método para actualizar el estado
    def actualizar(self, nuevo_estado: Estado) -> None:
        self.estado = nuevo_estado
        # Mostramos tanto el nombre simbólico como el valor entero
        print(f"📦 ID {self.id}: Estado -> {self.estado.name} ({self.estado.value})")

# 3. Uso y simulación
mi_paquete = Paquete("GTX987")

mi_paquete.actualizar(Estado.EN_TRANSITO)
mi_paquete.actualizar(Estado.EN_REPARTO)
mi_paquete.actualizar(Estado.ENTREGADO) 