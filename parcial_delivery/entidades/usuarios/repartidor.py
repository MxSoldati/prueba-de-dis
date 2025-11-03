# /parcial_delivery/entidades/usuarios/repartidor.py
from dataclasses import dataclass
from .usuario import Usuario

@dataclass
class Repartidor(Usuario):
    """ Entidad Repartidor (hereda de Usuario) """
    tipo_vehiculo: str # ej. "Moto", "Bicicleta"
    disponible: bool = True