class Tiquete:
    def __init__(self, pasajero, vuelo, precio_base):
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.precio_base = precio_base
        self.precio_pagado = precio_base
        self.costo_equipaje_extra = 0
        self.estado = "Activo"

    def cancelar(self):
        self.estado = "Cancelado"

    def hacer_check_in(self, peso_maletas, cargas_especiales=[]):
        peso_maximo = 0
        costo_kilo_extra = 0

        if self.pasajero.clase == "Economica":
            peso_maximo = 10
            costo_kilo_extra = 5000
        elif self.pasajero.clase == "Ejecutiva":
            peso_maximo = 20
            costo_kilo_extra = 10000
        elif self.pasajero.clase == "Premium":
            peso_maximo = 30
            costo_kilo_extra = self.precio_base * 0.01

        exceso = peso_maletas - peso_maximo

        if exceso > 0:
            if self.pasajero.clase == "Premium":
                costo_exceso = exceso * costo_kilo_extra
            else:
                costo_exceso = exceso * costo_kilo_extra
            self.costo_equipaje_extra += costo_exceso

        for carga in cargas_especiales:
            if carga.tipo.lower() == "bicicleta":
                costo = carga.peso * 3000
                self.costo_equipaje_extra += costo
            elif carga.tipo.lower() == "perro":
                costo = self.precio_base * 0.05
                self.costo_equipaje_extra += costo
            elif carga.tipo.lower() == "gato":
                costo = self.precio_base * 0.02
                self.costo_equipaje_extra += costo

        self.precio_pagado += self.costo_equipaje_extra

