"""
Archivo integrador generado automaticamente
Directorio: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/usuarios
Fecha: 2025-11-03 20:15:08
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/usuarios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: servicio_usuarios.py
# Ruta: /Users/mxsoldati/Desktop/ParcialDelivery/parcial_delivery/servicios/usuarios/servicio_usuarios.py
# ================================================================================

# /parcial_delivery/servicios/usuarios/servicio_usuarios.py
from typing import List
from parcial_delivery.entidades.usuarios.usuario import Usuario
from parcial_delivery.patrones.factory.usuario_factory import UsuarioFactory

class ServicioUsuarios:
    """
    Capa Controlador (Servicio de Dominio).
    Maneja la lógica de negocio para operar con Usuarios.
    Utiliza el Patrón Factory para la creación.
    """

    def __init__(self):
        print("ServicioUsuarios inicializado.")
        # (Usaremos una lista en memoria como 'base de datos' temporal)
        self._usuarios: List[Usuario] = []

    def crear_usuario(self, tipo: str, **kwargs) -> Usuario:
        """
        (Controlador) Pide a la Fábrica que cree un usuario.
        El servicio no sabe CÓMO se crea, solo pide.
        """
        print(f"SERVICIO: Recibida orden para crear usuario tipo '{tipo}'.")
        
        # --- ¡AQUÍ USA EL PATRÓN FACTORY! ---
        nuevo_usuario = UsuarioFactory.crear_usuario(tipo, **kwargs)
        # ------------------------------------
        
        self._usuarios.append(nuevo_usuario)
        print(f"SERVICIO: Usuario {nuevo_usuario.id_usuario} ({nuevo_usuario.nombre}) creado.")
        return nuevo_usuario

