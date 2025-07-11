import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from ventana import Ventana

class Aplicacion(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        win = Ventana(self)
        win.present()

app = Aplicacion()
app.run()
