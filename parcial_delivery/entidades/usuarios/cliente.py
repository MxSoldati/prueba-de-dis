# /parcial_delivery/entidades/usuarios/cliente.py
from dataclasses import dataclass
from .usuario import Usuario

@dataclass
class Cliente(Usuario):
    """ Entidad Cliente (hereda de Usuario) """
    direccion: str
    telefono: str