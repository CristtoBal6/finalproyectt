import numpy as np
import random
class Ambiente:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grilla = [[None for _ in range(columnas)] for _ in range(filas)]
        self.nutrientes = np.random.randint(15, 25, (filas, columnas))
        self.factor_ambiental = np.zeros((filas, columnas))  

    def actualizar_nutrientes(self):
        self.nutrientes += np.random.randint(0, 5, (self.filas, self.columnas))

    def aplicar_ambiente(self, bacteria, i, j):
        if self.factor_ambiental[i][j] == 1 and not bacteria.resistente:
            if random.random() > 0.15:
                bacteria.morir()
        
