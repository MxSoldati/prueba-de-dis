# /parcial_delivery/patrones/factory/usuario_factory.py
from parcial_delivery.entidades.usuarios.usuario import Usuario
from parcial_delivery.entidades.usuarios.cliente import Cliente
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class UsuarioFactory:
    """
    Implementación del Patrón Factory Method.
    Encapsula la lógica de creación de diferentes tipos de usuarios.
    """
    
    _id_counter = 1

    @staticmethod
    def _next_id() -> int:
        """Helper interno para simular un ID autoincremental."""
        id = UsuarioFactory._id_counter
        UsuarioFactory._id_counter += 1
        return id

    @staticmethod
    def crear_usuario(tipo: str, **kwargs) -> Usuario:
        """
        El método fábrica.
        Recibe el 'tipo' y un diccionario de argumentos.
        """
        id_usuario = UsuarioFactory._next_id()
        
        if tipo == "Cliente":
            # Encapsula la lógica de construcción de Cliente
            if 'direccion' not in kwargs or 'telefono' not in kwargs:
                raise ValueError("Cliente requiere 'direccion' y 'telefono'")
            
            return Cliente(
                id_usuario=id_usuario,
                nombre=kwargs['nombre'],
                email=kwargs['email'],
                direccion=kwargs['direccion'],
                telefono=kwargs['telefono']
            )
            
        elif tipo == "Repartidor":
            # Encapsula la lógica de construcción de Repartidor
            if 'tipo_vehiculo' not in kwargs:
                raise ValueError("Repartidor requiere 'tipo_vehiculo'")
                
            return Repartidor(
                id_usuario=id_usuario,
                nombre=kwargs['nombre'],
                email=kwargs['email'],
                tipo_vehiculo=kwargs['tipo_vehiculo']
            )
        
        # (Aquí iría AdminRestaurante, etc.)

        else:
            raise ValueError(f"Tipo de usuario '{tipo}' desconocido")