import pandas as pd
import matplotlib.pyplot as plt

def analisar_meus_precos():
    arquivo = 'relatorio_precos.csv'
    
    try:
        df = pd.read_csv(arquivo)
        
        print("\n--- 🕵️ RELATÓRIO DO ANALISTA ---")
        print(df.head())

        media = df['Preco'].mean()
        maximo = df['Preco'].max()
        minimo = df['Preco'].min()
        
        print(f"📊 Média: R$ {media:.2f}")

        print("\n🎨 Gerando gráfico...")
        
        df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
        
        df.plot(x='Data', y='Preco', marker='o', color='pink', linestyle='-')
        plt.title('Variação do Dólar')
        plt.grid(True)
        plt.savefig('grafico_precos.png')
        
        print("🖼️ Gráfico salvo com sucesso: grafico_precos.png")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    analisar_meus_precos()