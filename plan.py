class Plan:
    """Plan de suscripción: nombre, precio y si muestra anuncios."""

    def __init__(self, nombre, precio, con_anuncios):
        self.nombre = nombre
        self.precio = precio
        self.con_anuncios = con_anuncios

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def tiene_anuncios(self):
        return self.con_anuncios

    def calcular_total(self, meses):
        """Precio total por varios meses (10% de descuento desde 12 meses)."""
        total = self.precio * meses
        if meses >= 12:
            total = total * 0.9
        return total

    def mostrar_info(self):
        anuncios = "con anuncios" if self.con_anuncios else "sin anuncios"
        return f"Plan {self.nombre} - ${self.precio}/mes ({anuncios})"
    
BASICO = Plan("Basico", 9.99, True)
PREMIUM = Plan("Premium", 13.99, False)