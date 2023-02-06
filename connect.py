import httpx 


class connectAPI:
    def __init__(self, base_currency) :
        self.isConnected = False       
        try:
            self.response = httpx.get(
                url=f'https://api.exchangerate.host/latest?base={base_currency}'
            ).json()
            self.currency_data = self.response['rates']
            self.isConnected = True
        except httpx.ConnectError:
            self.isConnected = False 
    
    def cotacao(self, currency):
        if self.isConnected:
            return self.currency_data.get(currency)
        else:
            return 'Não foi possivel executar a conversão'
    
    def moedas(self):
        moedas = []
        if self.isConnected:
            for moeda in self.currency_data:
                moedas.append(moeda)
        return moedas

