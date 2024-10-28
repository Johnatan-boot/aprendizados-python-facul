#DESENVOLVIMENTO MOBILE COM KVIDY
from kivy.app import app
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivimd.uix.button import MDRaisedButton
from kivimd.uix.textfield import MDTextField
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

Builder.load_string('''
<TabsLayout>:
TabbedPanel:
  do_default_tab: False
  TabbedPanelItem:
  text: 'Tab 1'
  BoxLayout:
    orientation: 'vertical'
    Label:
      text:'content for Tab 1'
   TabbedPanelItem:
   text: 'Tab 2'
   BoxLayout:
       orientation: 'vertical'
       Label:
       text: 'Content for Tab 2'   
''')

class TabsLayout(BoxLayout):
    pass
class TabsApp(App):
    def build(self):
        return TabsLayout()

# Função de inicialização
def run_kivy_app():
    app = TabsApp()
    app.run()

#Chame a função para executar o aplicativo
run_kivy_app()



#Definindo a string KV  que contém a descrição da interface
KV = '''
<CalculatorApp>:
    orientation: 'vertical'
    MDTextFIELD:
    id: input_field
    hint_text: "Insíra um número"
    helper_text_mode: "on_focus"
    input_filter: "float"
  GridLayout:
  cols:4
  spacing: dp(10)
  MDRaisesButton:
      text: "1"
      on_press: app.on_number_press(1)
  MDRaisedButton:
      text: "2"
      on_press: app.on_number_press(2)
  MDRaisedButton:
      text: "3"
      on_press: app.on_number_press(3)
  MDRaisedButton:
      text: "+"
      on_press: app.on_number_press(+)    
  MDRaisedButton:
      text: "4"
      on_press: app.on_operator_press(4)
  MDRaisedButton:
      text: "5"
      on_press: app.on_number_press(5)
  MDRaisedButton:
      text: "6"
      on_press: app.on_number_press(6)
  MDRaisedButton:
      text: "-"
      on_press: app.on_number_press(-)        
  MDRaisedButton:
      text: "7"
      on_press: app.on_number_press(7)
  MDRaisedButton:
      text: "8"
      on_press: app.on_number_press(8)
  MDRaisedButton:
      text: "9"
      on_press: app.on_number_press(9)  
  MDRaisedButton:
      text: "*"
      on_press: app.on_clear_input(*)
  MDRaisedButton:
      text: "C"
      on_press: app.clear_input()
  MDRaisedButton:
      text: "0"
      on_press: app.on_number_press(0)
  MDRaisedButton:
      text: "="
      on_press: app.calculate_result()
  MDRaisedButton:
      text: "/"
      on_press: app.on_operator_press("/")                                                                

'''

#DEFININDO A CLASSE CALCULATORAPP QUE HERDA DE BOXLAYOUT
class CalculatorApp(BoxLayout):
    # METODO CHAMADO QUANDO UM NÚMERO É  PRESSIONADO
    def on_number_press(self,number):
        current_text = self.ids.input_field.text
        new_text = f"{current_text}{number}"
        self.ids.input_field_text = new_text

    #METODO CHAMADO QUANDO UM OPERATOR É PRESSIONADO
    def on_operator_press(self, operator):
        current_text = self.ids.input_field_text
        new_text = f"{current_text} {operator}"
        self.ids.input_field_text = new_text

    #METODO CHAMADO PARA LIMPAR A ENTRADA
    def clear_input(self):
        self.ids.input_field_text = ""

    #METODO CHAMADO PARA CALCULAR O RESULTADO DA EXPRESSÃO
    def calculate_result(self):
        try:
            result = eval(self.ids.input_field.text)
            self.ids.input_field.text  = str(result)
        except Exception as  e:
            self.ids.input_field.text = "Erro"


