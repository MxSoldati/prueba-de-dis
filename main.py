# /main.py
# -----------------------------------------------------------------
# VISTA (MAIN) - Simulación del Sistema de Delivery
# -----------------------------------------------------------------
# Este archivo actúa como la 'Vista' o el 'Cliente' que dispara
# las acciones, siguiendo la arquitectura MVC/MVS (Modelo-Vista-Servicio).
#
# IMPORTANTE: Como nuestro código está en el paquete 'parcial_delivery',
# todas las importaciones deben empezar con 'parcial_delivery.'
#
# from parcial_delivery.servicios.servicio_pedidos import ServicioPedidos
# from parcial_delivery.entidades.pedidos.pedido import Pedido

def imprimir_encabezado(titulo: str):
    """Función helper para imprimir un título prolijo."""
    print("\n" + "=" * 80)
    print(f"|| {titulo.upper()} ||")
    print("=" * 80)

def imprimir_patron(nombre: str, descripcion: str):
    """Función helper (¡como la de tu amigo!) para 'apuntar' al patrón."""
    print(f"\n   [... Aplicando Patrón {nombre.UPPER()} ...]")
    print(f"   [... {descripcion} ...]")

# -----------------------------------------------------------------
# INICIO DE LA SIMULACIÓN
# -----------------------------------------------------------------

imprimir_encabezado("Inicio de Simulación: Sistema de Pedidos")

print("\n¡Esqueleto del proyecto creado!")
print("Editando 'main.py' para empezar la simulación...")

# --- Aquí comenzará la lógica de la demo ---

# 1. Inicializar Servicios
# servicio_pedidos = ServicioPedidos()

# 2. Demostrar Patrón Factory (HU-4)
# ...

# 3. Demostrar Patrón State y Observer (HU-1, HU-2)
# ...

# 4. Demostrar Patrón Decorator (HU-3)
# ...

# 5. Demostrar Patrón Strategy (HU-5)
# ...


imprimir_encabezado("Fin de la Simulación")