"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: cliente.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/cliente.py
# ================================================================================

# /parcial_delivery/entidades/usuarios/cliente.py
from dataclasses import dataclass
from .usuario import Usuario

@dataclass
class Cliente(Usuario):
    """ Entidad Cliente (hereda de Usuario) """
    direccion: str
    telefono: str

# ================================================================================
# ARCHIVO 3/4: repartidor.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/repartidor.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: usuario.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/entidades/usuarios/usuario.py
# ================================================================================

# /parcial_delivery/entidades/usuarios/usuario.py
from dataclasses import dataclass

@dataclass
class Usuario:
    """ Clase base para todos los usuarios (Modelo) """
    id_usuario: int
    nombre: str
    email: str

