import requests

#Para criar uma funcao , utilzamos o comando def
def get_moedas():
    #URL da api
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    try:
        dados = requests.get(url)

        resposta = dados.json()
        
        #Realiza a busca de informações dentre do dicionario secundário
        valor_moeda_base = resposta['rates']['BRL']

        valor_dolar = resposta['rates']['USD']
        valor_euro = resposta['rates']['EUR']
    
        #realizando a conversão de moedas
        dolar = valor_moeda_base / valor_dolar 
        euro = valor_moeda_base / valor_euro
        return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} = 1 BRL"
    except:
        return ("Não foi possivel realizar a conversão de valores")
    
print(get_moedas())