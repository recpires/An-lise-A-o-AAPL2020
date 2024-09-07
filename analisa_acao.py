import yfinance as yf
import pandas as pd

def obter_dados_acao(ticker, dt_inicial, dt_final):
    try:
        dados = yf.Ticker(ticker)
        tabela = dados.history(start=dt_inicial, end=dt_final)
        return tabela
    except Exception as e:
        print(f"Erro ao buscar dados da ação {ticker}: {e}")
        return pd.DataFrame()

# Solicita os dados ao usuário
ticker = input("Digite o código da Ação: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
dt_final = input("Digite a data final (aaaa-mm-dd): ")

# Chama a função e exibe os resultados
resultado = obter_dados_acao(ticker, dt_inicial, dt_final)