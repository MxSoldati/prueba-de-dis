# /main.py
# -----------------------------------------------------------------
# VISTA (MAIN) - Simulación del Sistema de Delivery
# -----------------------------------------------------------------
# Demostración del Patrón State (HU-1) y Observer (HU-2)

from parcial_delivery.servicios.pedidos.servicio_pedidos import ServicioPedidos
# ¡NUEVA IMPORTACIÓN!
from parcial_delivery.notificaciones.notificador_cliente import NotificadorCliente

def imprimir_encabezado(titulo: str):
    """Función helper para imprimir un título prolijo."""
    print("\n" + "=" * 80)
    print(f"|| {titulo.upper()} ||")
    print("=" * 80)

def imprimir_patron(nombre: str, descripcion: str):
    """Función helper para 'apuntar' al patrón."""
    print(f"\n   [... Aplicando Patrón {nombre.upper()} ...]")
    print(f"   [... {descripcion} ...]")

# -----------------------------------------------------------------
# INICIO DE LA SIMULACIÓN
# -----------------------------------------------------------------

imprimir_encabezado("Inicio de Simulación: Sistema de Pedidos (HU-1 y HU-2)")

# --- 0. Inicializar el Controlador ---
print("\n[VISTA] -> Inicializando el ServicioPedidos (Controlador)...")
servicio_pedidos = ServicioPedidos()

# --- 1. Prueba de cancelación (exitosa) ---
# (Esta parte queda igual, para demostrar HU-1)
imprimir_patron("STATE", "HU-1: Probando cancelación en estado 'Pendiente'")
print("\n[VISTA] -> Pidiendo al Servicio que cree un pedido...")
pedido_1 = servicio_pedidos.crear_pedido(
    cliente="Valentín",
    items=["Pizza Muzza"],
    costo_base=1000.0
)
print(f"[VISTA] -> Solicitando al servicio cancelar el pedido 101...")
servicio_pedidos.cancelar_pedido(101)

print("\n" + "-" * 80)

# --- 2. Prueba de Observer (HU-2) y State (HU-1) ---

imprimir_patron("STATE / OBSERVER", "HU-1 y HU-2: Flujo de pedido con notificaciones")

print("\n[VISTA] -> Pidiendo al Servicio que cree un segundo pedido...")
pedido_2 = servicio_pedidos.crear_pedido(
    cliente="Alberto (Profe)",
    items=["Lomo Completo"],
    costo_base=1500.0
)
print(f"[VISTA] -> Pedido {pedido_2.id_pedido} creado.")

# --- ¡NUEVA SECCIÓN OBSERVER! ---
imprimir_patron("OBSERVER", "HU-2: Suscribiendo un Notificador al pedido 102")

# 2a. Creamos el Observador
notificador_profe = NotificadorCliente(cliente_telefono="+54 9 261 111-2222")

# 2b. La Vista le pide al Servicio que suscriba el Observador al Modelo
print("\n[VISTA] -> Solicitando al servicio suscribir el Notificador al pedido 102...")
servicio_pedidos.suscribir_a_pedido(pedido_2.id_pedido, notificador_profe)
# ----------------------------------

print("\n[VISTA] -> Solicitando al servicio AVANZAR el pedido 102 (Restaurante acepta)...")
# (Esto debe disparar la notificación)
servicio_pedidos.avanzar_estado_pedido(102)
print(f"[VISTA] -> Consultando estado: {servicio_pedidos.get_estado_pedido(102)}")


print("\n[VISTA] -> Solicitando al servicio CANCELAR el pedido 102 (HU-1)...")
# (Prueba de State: esto debe fallar)
servicio_pedidos.cancelar_pedido(102)
print(f"[VISTA] -> Consultando estado: {servicio_pedidos.get_estado_pedido(102)}")


imprimir_encabezado("Fin de la Simulación (HU-1 y HU-2 Demostradas)")
print("\n   ✓ Demostrado: El Patrón STATE bloquea 'cancelar()' en 'En Preparación'.")
print("   ✓ Demostrado: El Patrón OBSERVER notifica automáticamente al cliente.")
print("   ✓ Demostrado: El Pedido (Sujeto) no sabe que existe el Notificador (Observador).\n")