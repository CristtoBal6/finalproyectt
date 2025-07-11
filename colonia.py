from bacteria import Bacteria
import pandas as pd

class Colonia:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.historial = []

    def paso(self):
        nuevas = []
        for i in range(self.ambiente.filas):
            for j in range(self.ambiente.columnas):
                b = self.ambiente.grilla[i][j]
                if b and b.estado == "activa":
                    b.alimentar(self.ambiente.nutrientes[i][j])
                    self.ambiente.nutrientes[i][j] = 0
                    self.ambiente.aplicar_ambiente(b, i, j)

                    if b.energia < 10:
                        b.morir()
                    else:
                        hija = b.dividirse()
                        if hija:
                            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                                if 0 <= x < self.ambiente.filas and 0 <= y < self.ambiente.columnas:
                                    if self.ambiente.grilla[x][y] is None:
                                        self.ambiente.grilla[x][y] = hija
                                        break
        self.reporte_estado()

    def reporte_estado(self):
        vivos = sum(1 for fila in self.ambiente.grilla for b in fila if b and b.estado == "activa")
        muertos = sum(1 for fila in self.ambiente.grilla for b in fila if b and b.estado == "muerta")
        resistentes = sum(1 for fila in self.ambiente.grilla for b in fila if b and b.estado == "activa" and b.resistente)
        self.historial.append({"vivos": vivos, "muertos": muertos, "resistentes": resistentes})

    def exportar_csv(self):
        pd.DataFrame(self.historial).to_csv("reporte.csv", index=False)
