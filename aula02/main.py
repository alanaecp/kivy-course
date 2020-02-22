from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        botao = Button(text="Botão 1")
        texto = Label(text="Texto 1")

        box2 = BoxLayout()
        box2.add_widget(Label(text="Texto 2"))
        box2.add_widget(Button(text="Botão 2"))
        box.add_widget(texto)
        box.add_widget(botao)
        box.add_widget(box2)
        return box

Test().run()