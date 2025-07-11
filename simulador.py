import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from colonia import Colonia
from bacteria import Bacteria
import random 
import pandas as pd

class Simulador:
    def __init__(self, ambiente):
        self.colonia = Colonia(ambiente)
        self.ambiente = ambiente
        self.paso_actual = 0
        self.finalizado = False

    def iniciar(self, cantidad=20):
        for _ in range(cantidad):
            while True:
                i = random.randint(0, self.ambiente.filas-1)
                j = random.randint(0, self.ambiente.columnas-1)
                if self.ambiente.grilla[i][j] is None:
                    self.ambiente.grilla[i][j] = Bacteria("A", 50)
                    break
        self.definir_zonas_antibiotico()

    def definir_zonas_antibiotico(self):
        for _ in range(10):
            i = random.randint(0, self.ambiente.filas-1)
            j = random.randint(0, self.ambiente.columnas-1)
            if self.ambiente.grilla[i][j] is None:
                self.ambiente.factor_ambiental[i][j] = 1

    def run(self, pasos=1):
        if self.finalizado:
            return
        for _ in range(pasos):
            self.ambiente.actualizar_nutrientes()
            self.colonia.paso()
            self.paso_actual += 1
            if self.colonia.historial[-1]["vivos"] == 0:
                self.finalizado = True
                break

    def graficar_grilla(self):
        matriz = np.zeros((self.ambiente.filas, self.ambiente.columnas))
        nutrientes = self.ambiente.nutrientes

        for i in range(self.ambiente.filas):
            for j in range(self.ambiente.columnas):
                b = self.ambiente.grilla[i][j]
                if b:
                    if b.estado == "muerta":
                        matriz[i][j] = 2
                    elif b.resistente:
                        matriz[i][j] = 3
                    else:
                        matriz[i][j] = 1
                elif self.ambiente.factor_ambiental[i][j] == 1:
                    matriz[i][j] = 4

        cmap = plt.cm.get_cmap('Set1', 5)
        fig, ax = plt.subplots(figsize=(7, 7))
        cax = ax.imshow(matriz, cmap=cmap, interpolation='nearest')

        legend_elements = [
            Patch(facecolor=cmap(1/5), label='1: Activa'),
            Patch(facecolor=cmap(2/5), label='2: Muerta'),
            Patch(facecolor=cmap(3/5), label='3: Resistente'),
            Patch(facecolor=cmap(4/5), label='4: Antibiótico'),
        ]

        ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.35, 1))
        ax.set_xticks(np.arange(self.ambiente.columnas))
        ax.set_yticks(np.arange(self.ambiente.filas))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xticks(np.arange(-.5, self.ambiente.columnas, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.ambiente.filas, 1), minor=True)
        ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
        ax.tick_params(which='both', bottom=False, left=False)

        for i in range(self.ambiente.filas):
            for j in range(self.ambiente.columnas):
                valor = matriz[i][j]
                if valor > 0:
                    ax.text(j, i, str(int(valor)), ha='center', va='center', color='white', fontsize=10, weight='bold')
                else:
                    nivel = nutrientes[i][j]
                    if nivel > 0:
                        ax.text(j, i, str(int(nivel)), ha='center', va='center', color='black', fontsize=8)

        plt.title(f"Paso {self.paso_actual}: Simulación bacteriana")
        plt.tight_layout()
        plt.savefig("grilla.png")
        plt.close()

    def graficar_resumen(self):
        df = pd.DataFrame(self.colonia.historial)
        df.plot()
        plt.title("Evolución de la colonia")
        plt.xlabel("Paso")
        plt.ylabel("Cantidad")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("grafico_evolucion.png")
        plt.close()
