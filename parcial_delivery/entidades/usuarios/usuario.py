# /parcial_delivery/entidades/usuarios/usuario.py
from dataclasses import dataclass

@dataclass
class Usuario:
    """ Clase base para todos los usuarios (Modelo) """
    id_usuario: int
    nombre: str
    email: str