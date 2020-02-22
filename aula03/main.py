from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        botao = Button(text="Botao 1", font_size=30, on_release=self.incrementar)
        self.label = Label(text="1", font_size=30)

        box.add_widget(self.label)
        box.add_widget(botao)
        return box

    def incrementar(self,button):
       self.label.text = str(int(self.label.text) + 1)


Test().run()