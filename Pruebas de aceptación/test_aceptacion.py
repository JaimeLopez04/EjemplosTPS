# test_aceptacion.py
import pytest
from carrito import CarritoDeCompras

def test_agregar_producto_al_carrito():
    # Escenario de prueba: Un usuario agrega un producto al carrito
    carrito = CarritoDeCompras()
    producto = "Camiseta"
    carrito.agregar_producto(producto)

    # Verificación: El producto debe estar en el carrito
    assert producto in carrito.productos

def test_eliminar_producto_del_carrito():
    # Escenario de prueba: Un usuario elimina un producto del carrito
    carrito = CarritoDeCompras()
    producto = "Zapatillas"
    carrito.agregar_producto(producto)
    carrito.eliminar_producto(producto)

    # Verificación: El producto no debe estar en el carrito
    assert producto not in carrito.productos
