from modelos.aerolinea import Aerolinea
from modelos.vuelo import Vuelo
from modelos.tiquete import Tiquete
from modelos.pasajero import Pasajero
from modelos.carga_especial import CargaEspecial

aerolinea = Aerolinea("Mi Aerolínea")

vuelo1 = Vuelo("Bogotá", "Madrid")
aerolinea.agregar_vuelo(vuelo1)

pasajero1 = Pasajero("Ana", 30, "F", "Economica")
tiquete1 = Tiquete(pasajero1, vuelo1, 2000000)

vuelo1.vender_tiquete(tiquete1)

peso_maletas = 15
cargas = [
    CargaEspecial("bicicleta", 10)
]

tiquete1.hacer_check_in(peso_maletas, cargas)

trayecto, dinero = aerolinea.trayecto_mas_recaudado()
print("Trayecto que más recaudó:", trayecto, "con", dinero, "pesos")

genero = aerolinea.genero_mayoritario_a_destino("Madrid")
print("Mayoría que viaja a Madrid:", genero)

promedios = aerolinea.costo_promedio_por_trayecto()
for trayecto, promedio in promedios:
    print("Trayecto:", trayecto, "Promedio de precio:", promedio)

total_tiquetes = aerolinea.recaudo_total_tiquetes()
print("Total recaudado por tiquetes:", total_tiquetes)

total_equipaje = aerolinea.recaudo_total_equipaje_extra()
print("Total recaudado por equipaje extra:", total_equipaje)
