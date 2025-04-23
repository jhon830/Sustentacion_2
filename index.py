from modelos.vuelo import Vuelo
from modelos.pasajero import PasajeroEconomica, PasajeroEjecutiva, PasajeroPremium
from modelos.equipaje import Equipaje
from modelos.carga_especial import CargaEspecial

def main():
    try:
        vuelo1 = Vuelo("Bogotá", "Madrid")
        print("Vuelo creado correctamente")

        
        pasajero1 = PasajeroEconomica("Juan Pérez", 30, "masculino", 1000000)
        print("PasajeroEconomica creado correctamente")
        
        
        pasajero2 = PasajeroEjecutiva("Ana Gómez", 42, "femenino", 2000000)
        print("PasajeroEjecutiva creado correctamente")
        
        
        pasajero3 = PasajeroPremium("Carlos López", 35, "masculino", 3000000)
        print("PasajeroPremium creado correctamente")

        
        equipaje1 = Equipaje(15)
        pasajero1.agregar_equipaje(equipaje1)
        print("Equipaje agregado a pasajero económico correctamente")
        
        equipaje2 = Equipaje(25)
        pasajero2.agregar_equipaje(equipaje2)
        print("Equipaje agregado a pasajero ejecutivo correctamente")
        
        equipaje3 = Equipaje(35)
        pasajero3.agregar_equipaje(equipaje3)
        print("Equipaje agregado a pasajero premium correctamente")

        
        carga1 = CargaEspecial("bicicleta", 10, 2000)
        pasajero1.agregar_carga_especial(carga1)
        print("Carga especial agregada correctamente")

       
        vuelo1.agregar_pasajero(pasajero1)
        vuelo1.agregar_pasajero(pasajero2)
        vuelo1.agregar_pasajero(pasajero3)
        print("Pasajeros agregados al vuelo correctamente")

        
        print("\nInformación de pasajeros:")
        print(f"Económica - Valor del tiquete: {pasajero1.get_valor_tiquete()} pesos")
        print(f"Ejecutiva - Valor del tiquete: {pasajero2.get_valor_tiquete()} pesos")
        print(f"Premium - Valor del tiquete: {pasajero3.get_valor_tiquete()} pesos")
        
        print("\nCostos adicionales:")
        print(f"Económica - Costo equipaje adicional: {pasajero1.calcular_costo_equipaje_adicional()} pesos")
        print(f"Ejecutiva - Costo equipaje adicional: {pasajero2.calcular_costo_equipaje_adicional()} pesos")
        print(f"Premium - Costo equipaje adicional: {pasajero3.calcular_costo_equipaje_adicional()} pesos")
        
        print(f"\nRecaudo total del vuelo: {vuelo1.recaudo_total()} pesos")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()  

if __name__ == "__main__":
    main()
