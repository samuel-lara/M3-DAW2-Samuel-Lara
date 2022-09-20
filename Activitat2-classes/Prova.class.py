class Beguda:

    def __init__(self, name):  # atributs
        self.name = name

    def getDetail(self):
        return self.name


class Producte:

    def __init__(self, cost, price):
        self.cost = cost
        self.price = price

    def getGain(self):
        # f es igual a un métode que permet formatar en text el que passem dins de les { }, també funciona ficant .format() al final del string
        return f"Les ganancies son de {self.price-self.cost}€"


class Estrella(Beguda, Producte):  # Hereda de las dos clases

    def __init__(self, name, brand, alcohol, cost, price):  # Constructor
        Beguda.__init__(self, name)  # __init__ para heredarlas de otra clase
        Producte.__init__(self, cost, price)
        self.__brand = brand
        self.__alcohol = alcohol

    def getDetail2(self):
        return f"La beguda {self.name} de la marca {self.__brand}, conté {self.__alcohol}% d'alcohol"


Nestea = Estrella('Nestea', 'Cocacola', 0, 0.29, 1.50)
print(Nestea.getDetail())
print(Nestea.getGain())
print(Nestea.getDetail2())
