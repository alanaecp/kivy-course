from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Python Kivy - adicionar Label dinamicamente e TextInput

class IMC(BoxLayout):
    pass
    def calcularIMC(self):
        peso = float(self.ids.peso.text)
        altura = float(self.ids.altura.text)
        imc = peso / altura **2
        if imc < 10:
            descr_imc = "Desnutrição Grau V"
        elif 10 < imc < 12.9:
            descr_imc = "Desnutrição Grau IV"
        elif 13 < imc < 15.9:
            descr_imc = "Desnutrição Grau III"
        elif 16 < imc < 16.9:
            descr_imc = "Desnutrição Grau II"
        elif 17 < imc < 18.4:
            descr_imc = "Desnutrição Grau I"
        elif 18.5 < imc < 24.9:
            descr_imc = "Normal"
        elif 25< imc < 29.9:
            descr_imc = "Pré-obesidade"
        elif 30 < imc < 34.5:
            descr_imc = "Obesidade Grau I"
        elif 35 < imc < 39.9:
            descr_imc = "Obesidade Grau II"
        elif imc > 40:
            descr_imc = "Obesidade Grau III"
        else:
            descr_imc = "Outros"

        self.ids.resultado.text = str(imc) + ": " + descr_imc


class Test(App):
    def build(self):
        return IMC()

Test().run()
