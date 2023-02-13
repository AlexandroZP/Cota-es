import csv
from connect import connectAPI


def save_currency(currencyBase,valueBase,valueCurrency,currency):
    document = read_document()
    for linha in document:
        if currencyBase in linha[0] and currency in linha[3]:
            print('Cotação já está salva')
            break
    else:
        with open('salvos.csv', 'a', newline='', encoding='utf-8') as saved:
            write = csv.writer(saved, delimiter=',')
            add = [currencyBase,valueBase,valueCurrency,currency]
            write.writerow(add)


def update_csv():
    document = read_document()
    add = []
    with open('salvos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        write = csv.writer(arquivo, delimiter=',')
        for linha in document:
            con = connectAPI(linha[0])
            linha[2] = con.cotacao(linha[3])
            add.append(linha)
        write.writerows(add)



def read_document():
    with open('salvos.csv', 'r') as file:
        read = csv.reader(file, delimiter=',')
        lines = []
        for line in read:
            lines.append(line)
        return lines
    

def delete_row(lista):
    document = read_document()
    with open('salvos.csv', 'w', newline='', encoding='utf-8') as arquivo:
        write = csv.writer(arquivo, delimiter=',')
        for linha in document:
            for item in lista:
                if linha[0] == item[0] and linha[3] == item[3]:
                    document.remove(linha)

        write.writerows(document)


