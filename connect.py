import httpx 
from PySimpleGUI import PySimpleGUI as sg


class connectAPI:
    def __init__(self, base_currency='USD'):
        self._isConnected = False              
        try:
            self.response = httpx.get(
                url=f'https://api.exchangerate.host/latest?base={base_currency}'
            ).json()
            self.currency_data = self.response['rates']
            self._isConnected = True
        except httpx.ConnectError:
            self._isConnected = False 
    
    @property
    def _isConnected(self):
        return self.isConnected
    
    @_isConnected.setter
    def _isConnected(self, value):
        self.isConnected = value

    def moedas(self):
        moedas = []
        for moeda in self.currency_data:
            moedas.append(moeda)
        return moedas
    
    def cotacao(self, currency):
        return self.currency_data.get(currency)

        

