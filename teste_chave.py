from dotenv import load_dotenv

load_dotenv ()

chave = load_dotenv()

if chave:
    print(f"A Chave foi carregada com sucesso!!")
else:
    print("Falha ao carregar a chave")