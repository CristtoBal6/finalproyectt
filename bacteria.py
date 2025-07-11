import random

class Bacteria:
    contador_id = 0

    def __init__(self, raza, energia, resistente=False):
        self.id = Bacteria.contador_id
        Bacteria.contador_id += 1
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = "activa"

    def alimentar(self, nutrientes):
        self.energia += nutrientes

    def mutar(self):
        if random.random() < 0.05:
            self.resistente = True

    def dividirse(self):
        if self.energia >= 60:
            self.energia //= 2
            hija = Bacteria(self.raza, self.energia, self.resistente)
            hija.mutar()
            return hija
        return None

    def morir(self):
        self.estado = "muerta"
import random

class Bacteria:
    contador_id = 0

    def __init__(self, raza, energia, resistente=False):
        self.id = Bacteria.contador_id
        Bacteria.contador_id += 1
        self.raza = raza
        self.energia = energia
        self.resistente = resistente
        self.estado = "activa"

    def alimentar(self, nutrientes):
        self.energia += nutrientes

    def mutar(self):
        if random.random() < 0.05:
            self.resistente = True

    def dividirse(self):
        if self.energia >= 60:
            self.energia //= 2
            hija = Bacteria(self.raza, self.energia, self.resistente)
            hija.mutar()
            return hija
        return None

    def morir(self):
        self.estado = "muerta"
