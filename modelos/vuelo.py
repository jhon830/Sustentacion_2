class Vuelo:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def recaudo_total(self):
        return sum(pasajero.get_valor_tiquete() for pasajero in self.pasajeros)
