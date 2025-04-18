class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

    def trayecto_mas_recaudado(self):
        mayor_recaudo = 0
        trayecto = ""
        for vuelo in self.vuelos:
            if vuelo.recaudo_total > mayor_recaudo:
                mayor_recaudo = vuelo.recaudo_total
                trayecto = vuelo.origen + " - " + vuelo.destino
        return trayecto, mayor_recaudo

    def genero_mayoritario_a_destino(self, destino_buscar):
        mujeres = 0
        hombres = 0
        for vuelo in self.vuelos:
            if vuelo.destino == destino_buscar:
                for tiquete in vuelo.tiquetes_emitidos:
                    if tiquete.pasajero.genero.lower() == "f":
                        mujeres += 1
                    elif tiquete.pasajero.genero.lower() == "m":
                        hombres += 1
        if mujeres > hombres:
            return "Mujeres"
        elif hombres > mujeres:
            return "Hombres"
        else:
            return "Igual cantidad"

    def costo_promedio_por_trayecto(self):
        resultados = []
        for vuelo in self.vuelos:
            if vuelo.tiquetes_vendidos > 0:
                promedio = vuelo.recaudo_total / vuelo.tiquetes_vendidos
                trayecto = vuelo.origen + " - " + vuelo.destino
                resultados.append((trayecto, promedio))
        return resultados

    def recaudo_total_tiquetes(self):
        total = 0
        for vuelo in self.vuelos:
            for tiquete in vuelo.tiquetes_emitidos:
                total += tiquete.precio_base
        return total

    def recaudo_total_equipaje_extra(self):
        total = 0
        for vuelo in self.vuelos:
            for tiquete in vuelo.tiquetes_emitidos:
                total += tiquete.costo_equipaje_extra
        return total
