from PySimpleGUI import PySimpleGUI as sg
from connect import connectAPI
from salvos import save_currency, read_document, update_csv, delete_row,create_fiel

class Tela():
    def __init__(self):
        sg.theme('TanBlue')
        self.con = connectAPI()
        try:
            update_csv()
        except FileNotFoundError:
            create_fiel()
        self.saved = read_document()
        self._moedas_frame =[
            [sg.Combo(values=(self.con.moedas()), default_value = 'USD', size=(10,20), key='-BASE_CURRENCY-'),
             sg.Input('1.00', size=(20,10), disabled=True),
             sg.Text('='), 
             sg.Input('0.00', size=(20,10), key='-TEXTO_MOSTRAGEM-', change_submits=True,  disabled=True),
             sg.Combo(values=(self.con.moedas()), default_value = 'BRL', size=(10,20), key='-CURRENCY-'), 
             sg.Button('Converter', key='-CONVERT_BUTTON-')],
             [sg.Button('Acompanhar cotacao', key='-SALVAR-')]
        ]
        self._salvos_frame = [
            [sg.Table(values=self.saved,
                      headings=['Moeda Base','Valor moeda base','Valor moeda desejada','Moeda Desejada']
                      ,auto_size_columns=True, justification='center', num_rows=5,row_height=40, 
                      select_mode='extended',key='-CURRENCY_LIST-')],
            [sg.Button('Deletar', key='-DELETE-')]
        ]
        self.__layout = [
            [sg.Frame('Selecione as moedas:', self._moedas_frame)],
            [sg.Frame('Cotações salvas', self._salvos_frame)]
        ]


        self.janela = sg.Window('Tela de Cadastro', self.__layout)
        
        


        while True:
            events, values = self.janela.read()

            match(events):
                case None:
                    break
                
                case '-CONVERT_BUTTON-':
                    con = connectAPI(values['-BASE_CURRENCY-'])
                    if con._isConnected:
                        if values['-CURRENCY-'] in con.moedas() and values['-BASE_CURRENCY-'] in con.moedas():
                            self.janela['-TEXTO_MOSTRAGEM-'].update(value=con.cotacao(values['-CURRENCY-']))
                        else:
                            sg.popup('[ERROR]Digite uma moeda válida')
                    else:
                        sg.popup('[ERROR] De conexão com a API')
                
                case '-SALVAR-':
                    save_currency(values['-BASE_CURRENCY-'], 1.00, values['-TEXTO_MOSTRAGEM-'],values['-CURRENCY-'])
                    self.janela['-CURRENCY_LIST-'].update(values=read_document())

                case '-DELETE-':
                    lista = read_document()
                    list_2 = []
                    removeList = values['-CURRENCY_LIST-']
                    removeList.sort(reverse=True)
                    for index in removeList:
                        list_2.append(lista[index])
                        lista.pop(index)
                    list_2.sort(reverse=True)
                    delete_row(list_2)
                    self.janela['-CURRENCY_LIST-'].update(values=lista)