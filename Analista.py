import requests
import csv
from datetime import datetime
import os

def analisar_mercado():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    arquivo_nome = 'relatorio_precos.csv'
    
    try:
        resposta = requests.get(url)
        dados = response_json = resposta.json()
        
        preco = float(dados['USDBRL']['bid'])
        nome = dados['USDBRL']['name']
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        print("-" * 40)
        print(f"💰 Preço: R$ {preco:.2f} | 🕒 {data_hora}")
        
        arquivo_existe = os.path.isfile(arquivo_nome)
        with open(arquivo_nome, mode='a', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            if not arquivo_existe:
                escritor.writerow(['Data', 'Moeda', 'Preco'])
            escritor.writerow([data_hora, nome, preco])
        print(f"✅ Relatório atualizado!")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    analisar_mercado()