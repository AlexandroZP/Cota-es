from PySimpleGUI import PySimpleGUI as sg
from connect import connectAPI

class Tela():
    def __init__(self):
        sg.theme('TanBlue')
        self.con = connectAPI()
        self._moedas_frame =[
            [sg.Combo(values=(self.con.moedas()), default_value = 'USD', key='-BASE_CURRENCY-'),
             sg.Input('1.00', disabled=True),
             sg.Text('='), 
             sg.Input('0.00', key='-TEXTO_MOSTRAGEM-', change_submits=True, disabled=True),
             sg.Combo(values=(self.con.moedas()), default_value = 'BRL', key='-CURRENCY-'), 
             sg.Button('Converter', key='-CONVERT_BUTTON-')]
        ]
        self.__layout = [
            [sg.Frame('Selecione as moedas:', self._moedas_frame)],
        ]


        self.janela = sg.Window('Tela de Cadastro', self.__layout)


        while True:
            events, values = self.janela.read()

            match(events):
                case None:
                    break
                
                case '-CONVERT_BUTTON-':
                    con = connectAPI(values['-BASE_CURRENCY-'])
                    self.janela['-TEXTO_MOSTRAGEM-'].update(value=con.cotacao(values['-CURRENCY-']))