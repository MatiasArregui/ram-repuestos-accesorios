
def carrito_context(request):
    carrito = request.session.get('carrito', {})

    cantidad = 0

    for valor in carrito.values():
        try:
            cantidad += max(0, int(valor))
        except (TypeError, ValueError):
            continue

    return {
        'cantidadCarrito': cantidad
    }
