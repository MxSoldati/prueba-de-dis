# /main.py
# -----------------------------------------------------------------
# VISTA (MAIN) - Simulación del Sistema de Delivery
# -----------------------------------------------------------------
# Demostración de State (HU-1), Observer (HU-2) y Factory (HU-4)

from parcial_delivery.servicios.pedidos.servicio_pedidos import ServicioPedidos
# --- ¡NUEVAS IMPORTACIONES! ---
from parcial_delivery.servicios.usuarios.servicio_usuarios import ServicioUsuarios
from parcial_delivery.entidades.usuarios.cliente import Cliente
# -----------------------------
from parcial_delivery.notificaciones.notificador_cliente import NotificadorCliente

def imprimir_encabezado(titulo: str):
    print("\n" + "=" * 80)
    print(f"|| {titulo.upper()} ||")
    print("=" * 80)

def imprimir_patron(nombre: str, descripcion: str):
    print(f"\n   [... Aplicando Patrón {nombre.upper()} ...]")
    print(f"   [... {descripcion} ...]")

# -----------------------------------------------------------------
# INICIO DE LA SIMULACIÓN
# -----------------------------------------------------------------

imprimir_encabezado("Inicio de Simulación: Sistema de Pedidos (HU-1, 2, 4)")

# --- 0. Inicializar Controladores ---
print("\n[VISTA] -> Inicializando Controladores...")
servicio_pedidos = ServicioPedidos()
servicio_usuarios = ServicioUsuarios() # ¡Nuevo servicio!

# --- 1. Demostración Patrón Factory (HU-4) ---
imprimir_patron("FACTORY METHOD", "HU-4: Creando usuarios (Clientes)")

print("\n[VISTA] -> Pidiendo al ServicioUsuarios crear un Cliente...")
cliente_1 = servicio_usuarios.crear_usuario(
    tipo="Cliente",
    nombre="Valentín",
    email="valentin@email.com",
    direccion="Calle Falsa 123",
    telefono="261-456-7890"
)
print(f"[VISTA] -> Cliente creado: {cliente_1}")

print("\n[VISTA] -> Pidiendo al ServicioUsuarios crear un segundo Cliente...")
cliente_2 = servicio_usuarios.crear_usuario(
    tipo="Cliente",
    nombre="Alberto (Profe)",
    email="alberto@email.com",
    direccion="Av. Siempre Viva 742",
    telefono="261-111-2222"
)
print(f"[VISTA] -> Cliente creado: {cliente_2}")


# --- 2. Prueba de cancelación (exitosa) (HU-1) ---
imprimir_patron("STATE", "HU-1: Probando cancelación en estado 'Pendiente'")

print("\n[VISTA] -> Pidiendo al ServicioPedidos crear un pedido...")
pedido_1 = servicio_pedidos.crear_pedido(
    cliente=cliente_1, # ¡Pasamos el objeto Cliente!
    items=["Pizza Muzza"],
    costo_base=1000.0
)
print(f"[VISTA] -> Solicitando al servicio cancelar el pedido 101...")
servicio_pedidos.cancelar_pedido(101)

print("\n" + "-" * 80)

# --- 3. Prueba de Observer (HU-2) y State (HU-1) ---
imprimir_patron("STATE / OBSERVER", "HU-1 y HU-2: Flujo de pedido con notificaciones")

print("\n[VISTA] -> Pidiendo al ServicioPedidos crear un segundo pedido...")
pedido_2 = servicio_pedidos.crear_pedido(
    cliente=cliente_2, # ¡Pasamos el objeto Cliente!
    items=["Lomo Completo"],
    costo_base=1500.0
)
print(f"[VISTA] -> Pedido {pedido_2.id_pedido} creado.")

# Suscribir Observer (HU-2)
imprimir_patron("OBSERVER", "HU-2: Suscribiendo un Notificador al pedido 102")
notificador_profe = NotificadorCliente(cliente_telefono=cliente_2.telefono)
print("\n[VISTA] -> Solicitando al servicio suscribir el Notificador al pedido 102...")
servicio_pedidos.suscribir_a_pedido(pedido_2.id_pedido, notificador_profe)

# Avanzar Estado (Dispara Observer)
print("\n[VISTA] -> Solicitando al servicio AVANZAR el pedido 102 (Restaurante acepta)...")
servicio_pedidos.avanzar_estado_pedido(102)

# Probar cancelación (HU-1)
print("\n[VISTA] -> Solicitando al servicio CANCELAR el pedido 102 (HU-1)...")
servicio_pedidos.cancelar_pedido(102)
print(f"[VISTA] -> Consultando estado: {servicio_pedidos.get_estado_pedido(102)}")


imprimir_encabezado("Fin de la Simulación (HU-1, 2, 4 Demostradas)")
print("\n   ✓ Demostrado: El Patrón FACTORY crea diferentes usuarios.")
print("   ✓ Demostrado: El Patrón STATE bloquea 'cancelar()'.")
print("   ✓ Demostrado: El Patrón OBSERVER notifica automáticamente al cliente.\n")