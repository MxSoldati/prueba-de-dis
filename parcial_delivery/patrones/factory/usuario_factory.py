# /parcial_delivery/patrones/factory/usuario_factory.py
from parcial_delivery.entidades.usuarios.usuario import Usuario
from parcial_delivery.entidades.usuarios.cliente import Cliente
from parcial_delivery.entidades.usuarios.repartidor import Repartidor

class UsuarioFactory:
    # ... (_id_counter y _next_id quedan igual) ...
    _id_counter = 1
    @staticmethod
    def _next_id() -> int:
        id = UsuarioFactory._id_counter
        UsuarioFactory._id_counter += 1
        return id

    @staticmethod
    def crear_usuario(tipo: str, **kwargs) -> Usuario:
        id_usuario = UsuarioFactory._next_id()
        
        if tipo == "Cliente":
            # ... (esta parte queda igual) ...
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
            # --- ¡SECCIÓN MODIFICADA! ---
            if 'tipo_vehiculo' not in kwargs:
                raise ValueError("Repartidor requiere 'tipo_vehiculo'")
            return Repartidor(
                id_usuario=id_usuario,
                nombre=kwargs['nombre'],
                email=kwargs['email'],
                tipo_vehiculo=kwargs['tipo_vehiculo'],
                # Añadimos los nuevos campos (con valores por defecto si no vienen)
                ubicacion=kwargs.get('ubicacion', (0, 0)),
                pedidos_activos=kwargs.get('pedidos_activos', 0)
            )
            # ---------------------------
        else:
            raise ValueError(f"Tipo de usuario '{tipo}' desconocido")