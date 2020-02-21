from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
# from kivy.uix.button import Button
from kivy.uix.label import Label

# Python Kivy - ScroolView e SizeHint

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=50, size_hint_y=None, height=200))

class Test(App):
    def build(self):
        return Tarefas(['preparar matriz EAD', 'lançar notas', 'fazer compras', 'preparar matriz EAD', 'lançar notas', 'fazer compras', 'preparar matriz EAD', 'lançar notas', 'fazer compras'])

Test().run()