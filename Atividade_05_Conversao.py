import requests

def convert_moeda():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
        
    try:
        dados = requests.get(url)

        resposta = dados.json()
        
        moeda_base = resposta['rates']['USD']
        
        valor_real = resposta['rates']['BRL']
        valor_euros = resposta['rates']['EUR']
        valor_libras_esterlina = resposta['rates']['GBP']
        valor_peso_argentinos = resposta['rates']['ARS']
        
        reais = moeda_base * valor_real
        euros = moeda_base * valor_euros
        libras_esterlina = moeda_base * valor_libras_esterlina
        peso_argetinos = moeda_base * valor_peso_argentinos
        
        return f"1 dolar correspode a {reais:.2f} BRL | {euros:.2f} EUR | {libras_esterlina:.2f} GBP | {peso_argetinos:.2f} ARS - valor base {moeda_base}"
        #return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} = 1 BRL"
    except:
        print("erro")
        
print(convert_moeda())