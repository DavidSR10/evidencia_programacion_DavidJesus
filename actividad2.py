"""
Diseña las clases Cliente, Producto y Pedidos. Define atributos de instancia y de clase
para cada una de ellas. (5 puntos)
● Diseña una aplicación de consola que nos permite añadir los nuevos pedidos. Cada
pedido deberá luego ordenarse por fecha de pedido. (5 puntos)
● Diseña un método que muestre el nombre de cliente y el total de pedidos realizados
en euros (10 puntos)
● Crea un método que permita mostrar los productos sin IVA y con IVA incluido (el tipo
de IVA es 21 %) (5 puntos)
"""
from typing import List

class Cliente:
    _contador_clientes = 0

    def __init__(self, nombre: str, direccion: str):
        Cliente._contador_clientes += 1
        self._id_cliente = Cliente._contador_clientes
        self.nombre = nombre
        self.direccion = direccion

    @property
    def id_cliente(self) -> int:
        return self._id_cliente

    def __str__(self) -> str:
        return f"Cliente {self.id_cliente}: {self.nombre}, Dirección: {self.direccion}"

class Producto:
    def __init__(self, nombre: str, precio: float, iva: float = 21.0):
        self.nombre = nombre
        self.precio = precio
        self.iva = iva

    def precio_con_iva(self) -> float:
        return self.precio * (1 + self.iva / 100)

    def __str__(self) -> str:
        return f"{self.nombre}: {self.precio:.2f} € (IVA incluido: {self.precio_con_iva():.2f} €)"

class Pedido:
    _contador_pedidos = 0

    def __init__(self, cliente: Cliente, productos: List[Producto], fecha: str):
        Pedido._contador_pedidos += 1
        self._id_pedido = Pedido._contador_pedidos
        self.cliente = cliente
        self.productos = productos
        self.fecha = fecha

    def total_pedido(self) -> float:
        return sum(producto.precio_con_iva() for producto in self.productos)

    def __str__(self) -> str:
        return f"Pedido {self._id_pedido} - Cliente: {self.cliente.nombre}, Fecha: {self.fecha}, Total: {self.total_pedido():.2f} €"


def mostrar_resumen(cliente: Cliente, pedidos: List[Pedido]) -> None:
    total_pedidos = sum(pedido.total_pedido() for pedido in pedidos)
    print(f"\033[92m{cliente.nombre}:\033[0m Total de pedidos en euros: \033[93m{total_pedidos:.2f} €\033[0m")

def mostrar_productos_con_iva(productos: List[Producto]) -> None:
    print("\033[96mProductos con IVA:\033[0m")
    for producto in productos:
        print(producto)

def mostrar_productos_sin_iva(productos: List[Producto]) -> None:
    print("\033[96mProductos sin IVA:\033[0m")
    for producto in productos:
        print(f"{producto.nombre}: \033[94m{producto.precio:.2f} €\033[0m")

def ordenar_pedidos_por_fecha(pedidos: List[Pedido]) -> List[Pedido]:
    pedidos_ordenados = sorted(pedidos, key=lambda pedido: pedido.fecha)
    print("\n\033[95mPedidos ordenados por fecha de menor a mayor:\033[0m")
    for pedido in pedidos_ordenados:
        print(pedido)
    return pedidos_ordenados


def main() -> None:
    # Crear clientes
    cliente1 = Cliente("Cliente A", "Calle A, Ciudad")
    cliente2 = Cliente("Cliente B", "Calle B, Ciudad")

    # Crear productos
    producto1 = Producto("Producto 1", 10)
    producto2 = Producto("Producto 2", 20)

    # Crear pedidos
    pedidos = [
        Pedido(cliente1, [producto1, producto2], "2023-01-01"),
        Pedido(cliente2, [producto2], "2023-01-02")
    ]

    while True:
        print("\n--- \033[95mMenú\033[0m ---")
        print("\033[92m1. Añadir nuevo pedido\033[0m")
        print("\033[92m2. Mostrar pedidos ordenados por fecha\033[0m")
        print("\033[92m3. Salir\033[0m")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente_nombre = input("Ingrese el nombre del cliente: ")
            cliente_direccion = input("Ingrese la dirección del cliente: ")
            nuevo_cliente = Cliente(cliente_nombre, cliente_direccion)

            print("Productos disponibles:")
            print("1. Producto 1 - 10.00 €")
            print("2. Producto 2 - 20.00 €")

            productos_pedido = []
            while True:
                producto_opcion = input("Seleccione un producto (1 o 2) o ingrese 0 para finalizar: ")
                if producto_opcion == "0":
                    break
                elif producto_opcion in {"1", "2"}:
                    producto_elegido = producto1 if producto_opcion == "1" else producto2
                    productos_pedido.append(producto_elegido)
                    print(f"Producto {producto_elegido.nombre} añadido al pedido.")
                else:
                    print("Opción no válida. Intente de nuevo.")

            fecha_pedido = input("Ingrese la fecha del pedido (formato YYYY-MM-DD): ")

            nuevo_pedido = Pedido(nuevo_cliente, productos_pedido, fecha_pedido)
            pedidos.append(nuevo_pedido)
            print("Pedido añadido correctamente.")

        elif opcion == "2":
            pedidos_ordenados = ordenar_pedidos_por_fecha(pedidos)


        elif opcion == "3":
            print("\033[91mSaliendo del programa.\033[0m")
            break

        else:
            print("\033[91mOpción no válida. Intente de nuevo.\033[0m")


if __name__ == "__main__":
    main()

