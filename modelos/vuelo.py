class Vuelo:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.tiquetes_emitidos = []
        self.recaudo_total = 0
        self.tiquetes_vendidos = 0

    def vender_tiquete(self, tiquete):
        self.tiquetes_emitidos.append(tiquete)
        self.recaudo_total += tiquete.precio_pagado
        self.tiquetes_vendidos += 1
