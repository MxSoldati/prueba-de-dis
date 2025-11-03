# /parcial_delivery/entidades/usuarios/repartidor.py
from dataclasses import dataclass, field
from .usuario import Usuario
from typing import Tuple # ¡Importante!

@dataclass
class Repartidor(Usuario):
    """ Entidad Repartidor (hereda de Usuario) """
    tipo_vehiculo: str # ej. "Moto", "Bicicleta"
    disponible: bool = True
    
    # --- NUEVOS CAMPOS PARA PATRÓN STRATEGY ---
    # Usamos una tupla (x, y) para simular coordenadas
    ubicacion: Tuple[int, int] = field(default=(0, 0))
    pedidos_activos: int = 0
    # ------------------------------------------