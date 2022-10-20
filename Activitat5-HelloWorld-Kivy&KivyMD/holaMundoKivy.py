from kivy.app import App
from kivy.uix.label import Label

#importamos el modulo que permite dar tamaño a la ventana
from kivy.core.window import Window
Window.size = (300, 550) #damos tamaño a la ventana, estilo móvil


class HolaMundoKivy(App):
    def build(self):
        return Label(text='Hola Mundo Kivy')



if __name__ == '__main__':
    HolaMundoKivy().run()