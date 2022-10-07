class Animal():
    def __init__(self, especie, poblacion, ubicacion, edad):
        self.especie = especie
        self.poblacion = poblacion
        self.ubicacion = ubicacion
        self.edad = edad
        self.__despierto = True
    def __str__(self):
        return f"{self.especie},{self.poblacion},{self.ubicacion},{self.edad}, ¿Está despierto? {self.__despierto}"
    def Caminar(self):
        return print("El animal está caminando")
    def Despertar(self):
        if self.__despierto == True:
            return print("El animal se encuentra despierto")
        elif self.__despierto == False:
            return print("El animal está durmiendo")
    def Comer(self):
        return print("El animal está alimentándose")
    def Despierto(self, estado):
        self.__despierto = estado
class AnimalTerrestre(Animal):
    def __init__(self, especie, poblacion, ubicacion, edad, pesaje):
        super().__init__(especie, poblacion, ubicacion, edad)
        self.pesaje = pesaje
    def __str__(self):
        return super().__str__()+f', {self.pesaje}'
    def Acechar(self):
        return print("El animal está acechando a su presa")
class AnimalAcuatico(Animal):
    def __init__(self, especie, poblacion, ubicacion, edad, agallas):
        super().__init__(especie, poblacion, ubicacion, edad)
        self.agallas = agallas!= True
    def __str__(self):
        return super().__str__()+f' ¿Tiene agallas? {self.agallas}'
    def Respiracion(self):
        return print("El animal sobrevive en el agua por sus agallas")
class AnimalAereo(Animal):
    def __init__(self, especie, poblacion, ubicacion, edad, alas):
        super().__init__(especie, poblacion, ubicacion, edad)
        self.alas = alas!=True
    def __str__(self):
        return super().__str__()+f' ¿Vuela? {self.alas}'
    def Volar(self):
        return print("El animal vuela porque tiene alas")
print()
leopardo = AnimalTerrestre("Raza: Felino"," Poblado: 500000"," Ubicación: Brasil","Edad: 12"," Pesaje: 31 kg")
print(leopardo)
leopardo.Acechar()
leopardo.Comer()
leopardo.Despertar()
leopardo.Despierto(True)
leopardo.Despertar()
print()
aguila = AnimalAereo("Raza: Aguiloide"," Poblado: 20000"," Ubicación: Perú"," Edad: 20"," Pesaje: 10 kg")
print(aguila)
aguila.Despierto(True)
aguila.Despertar()
aguila.Volar()
aguila.Comer()
print()
nemo = AnimalAcuatico("Pez: Payaso"," Poblacion: 120000"," Ubicacion: ABAJOLAWA", " Edad: 4","")
print(nemo)
nemo.Respiracion()
nemo.Despierto(False)
nemo.Despertar()