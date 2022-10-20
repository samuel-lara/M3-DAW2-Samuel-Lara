from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

#importamos el modulo que permite dar tamaño a la ventana
from kivy.core.window import Window
Window.size = (300, 550) #damos tamaño a la ventana, estilo móvil


class holaMundoKivyMD(MDApp):
    def build(self):
        return MDLabel(text="Hola Mundo KivyMD", halign="center")


if __name__ == '__main__':
    holaMundoKivyMD().run()