from connect import connectAPI

base_currency = 'USD'
currency = 'EUR'
con = connectAPI(base_currency)
if con:
    print(con.cotacao(currency))
    print(con.moedas())