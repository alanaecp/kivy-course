from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
from kivy.uix.label import Label

# Python Kivy - Layouts dinâmicos e KWARG! https://youtu.be/CXZWmVU4VIc

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=50))

class Test(App):
    def build(self):
        return Tarefas(['preparar matriz EAD', 'lançar notas', 'fazer compras'], orientation='horizontal')

Test().run()