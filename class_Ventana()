import matplotlib
matplotlib.use('Agg')

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from ambiente import Ambiente
from simulador import Simulador
import subprocess
import os

class Ventana(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Simulación de Colonias Bacterianas")
        self.set_default_size(500, 200)

        self.ambiente = Ambiente(10, 10)
        self.simulador = Simulador(self.ambiente)
        self.simulador.iniciar()

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(main_box)

        self.menu_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, hexpand=True)

        self.btn_paso = Gtk.Button(label="▶ Siguiente paso")
        self.btn_paso.connect("clicked", self.on_siguiente_paso)

        self.btn_exportar = Gtk.Button(label="💾 Exportar CSV")
        self.btn_exportar.connect("clicked", self.on_exportar_csv)

        self.btn_grafico = Gtk.Button(label="📈 Ver gráfico")
        self.btn_grafico.connect("clicked", self.on_ver_grafico)

        self.menu_bar.append(self.btn_paso)
        self.menu_bar.append(self.btn_exportar)
        self.menu_bar.append(self.btn_grafico)

        main_box.append(self.menu_bar)

        self.label_estado = Gtk.Label(label="Simulación iniciada. Paso 0.")
        main_box.append(self.label_estado)

    def on_siguiente_paso(self, button):
        if not self.simulador.finalizado:
            self.simulador.run(1)
            self.simulador.graficar_grilla()
            self.simulador.graficar_resumen()
            paso = self.simulador.paso_actual
            self.label_estado.set_text(f"Paso {paso}: grilla y gráfico actualizados.")
            subprocess.run(["xdg-open", "grilla.png"])
        else:
            self.label_estado.set_text("Simulación finalizada. No hay bacterias vivas.")

    def on_exportar_csv(self, button):
        self.simulador.colonia.exportar_csv()
        self.label_estado.set_text("Reporte CSV exportado.")

    def on_ver_grafico(self, button):
        subprocess.run(["xdg-open", "grafico_evolucion.png"])

