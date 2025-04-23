class Pasajero:
    def __init__(self, nombre, edad, genero, valor_tiquete):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        self.__valor_tiquete = valor_tiquete
        self.__equipaje = None
        self.__carga_especial = []

    def agregar_equipaje(self, equipaje):
        self.__equipaje = equipaje

    def agregar_carga_especial(self, carga):
        self.__carga_especial.append(carga)

    def calcular_costo_equipaje_adicional(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def calcular_costo_carga_especial(self):
        costo_total = 0
        for carga in self.__carga_especial:
            if carga.tipo == 'bicicleta':
                costo_total += carga.peso * carga.costo_por_kilo
            elif carga.tipo == 'perro':
                costo_total += self.__valor_tiquete * 0.05
            elif carga.tipo == 'gato':
                costo_total += self.__valor_tiquete * 0.02
        return costo_total

    def get_valor_tiquete(self):
        return self.__valor_tiquete

    def get_equipaje(self):
        return self.__equipaje

class PasajeroEconomica(Pasajero):
    def __init__(self, nombre, edad, genero, valor_tiquete):
        super().__init__(nombre, edad, genero, valor_tiquete)
        
    def calcular_costo_equipaje_adicional(self):
        limite = 10
        costo_por_kilo = 5000
        kilos_adicionales = max(0, self.get_equipaje().peso - limite)
        return kilos_adicionales * costo_por_kilo

class PasajeroEjecutiva(Pasajero):
    def __init__(self, nombre, edad, genero, valor_tiquete):
        super().__init__(nombre, edad, genero, valor_tiquete)
        
    def calcular_costo_equipaje_adicional(self):
        limite = 20
        costo_por_kilo = 10000
        kilos_adicionales = max(0, self.get_equipaje().peso - limite)
        return kilos_adicionales * costo_por_kilo

class PasajeroPremium(Pasajero):
    def __init__(self, nombre, edad, genero, valor_tiquete):
        super().__init__(nombre, edad, genero, valor_tiquete)
    
    def calcular_costo_equipaje_adicional(self):
        limite = 30
        costo_por_kilo = self.get_valor_tiquete() * 0.01
        kilos_adicionales = max(0, self.get_equipaje().peso - limite)
        return kilos_adicionales * costo_por_kilo
