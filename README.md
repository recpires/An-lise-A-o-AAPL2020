# Análise da Ação AAPL - Janeiro/2020 a Dezembro/2020 - Imersão Semana do Pyton Empowedata

## Introdução
Este projeto tem como objetivo realizar uma análise detalhada da ação da Apple (AAPL) no período de janeiro a dezembro de 2020. Utilizando a linguagem Python e o ambiente Jupyter Notebook, foram coletados dados históricos da ação e aplicadas diversas técnicas de análise técnica e fundamentalista.

## Objetivo
* **Analisar o desempenho da ação AAPL** no período especificado.
* **Identificar tendências** de alta, baixa e consolidação.
* **Avaliar o impacto de eventos** relevantes no mercado sobre a ação.
* **Gerar insights** que possam auxiliar na tomada de decisão de investimentos.

## Metodologia
1. **Coleta de Dados:**
   * Utilização da biblioteca `yfinance` para coletar dados históricos da ação AAPL.
   * Definição do período de análise: Janeiro/2020 a Dezembro/2020.
2. **Análise Exploratória:**
   * Cálculo de indicadores técnicos como média móvel, bandas de Bollinger, RSI, etc.
   * Visualização dos dados através de gráficos e tabelas.
3. **Análise de Eventos:**
   * Identificação de eventos relevantes que impactaram o mercado e a ação AAPL.
   * Análise do impacto desses eventos nos preços da ação.
4. **Automação do Relatório:**
   * Criação de um relatório conciso e informativo em formato de texto.
   * Utilização das bibliotecas `pyautogui`, `pyperclip` e `webbrowser` para automatizar o envio do relatório por e-mail.

## Resultados
                                 Open        High         Low       Close  \
Date                                                                        
2020-01-02 00:00:00-05:00   71.878848   72.936750   71.624082   72.876091   
2020-01-03 00:00:00-05:00   72.099672   72.931916   71.941959   72.167610   
2020-01-06 00:00:00-05:00   71.284400   72.781468   71.032056   72.742645   
2020-01-07 00:00:00-05:00   72.752348   73.009542   72.179727   72.400528   
2020-01-08 00:00:00-05:00   72.102098   73.868497   72.102098   73.565201   
...                               ...         ...         ...         ...   
2020-12-23 00:00:00-05:00  129.375520  129.639820  128.024590  128.200806   
2020-12-24 00:00:00-05:00  128.553169  130.648080  128.337804  129.189468   
2020-12-28 00:00:00-05:00  131.166948  134.446358  130.697051  133.810059   
2020-12-29 00:00:00-05:00  135.141404  135.865804  131.509564  132.028397   
2020-12-30 00:00:00-05:00  132.723430  133.124795  130.589353  130.902618   

                              Volume  Dividends  Stock Splits  
Date                                                           
2020-01-02 00:00:00-05:00  135480400        0.0           0.0  
2020-01-03 00:00:00-05:00  146322800        0.0           0.0  
2020-01-06 00:00:00-05:00  118387200        0.0           0.0  
2020-01-07 00:00:00-05:00  108872000        0.0           0.0  
2020-01-08 00:00:00-05:00  132079200        0.0           0.0  
...                              ...        ...           ...  
2020-12-23 00:00:00-05:00   88223700        0.0           0.0  
2020-12-24 00:00:00-05:00   54930100        0.0           0.0  
2020-12-28 00:00:00-05:00  124486200        0.0           0.0  
2020-12-29 00:00:00-05:00  121047300        0.0           0.0  
2020-12-30 00:00:00-05:00   96452100        0.0           0.0  

[252 rows x 7 columns]

Fechamento Ano 2023
Date
2023-01-03    125.070000
2023-01-04    126.360001
2023-01-05    125.019997
2023-01-06    129.619995
2023-01-09    130.149994
                 ...    
2023-12-22    193.600006
2023-12-26    193.050003
2023-12-27    193.149994
2023-12-28    193.580002
2023-12-29    192.529999
Name: Close, Length: 250, dtype: float64

## Conclusões
Foram encontrado o valor máximo e o valor mínimo e realisado a média para uma análise mais completa

## Ferramentas Utilizadas
* **Python:** Linguagem de programação utilizada para realizar toda a análise.
* **Jupyter Notebook:** Ambiente interativo para desenvolvimento e execução do código Python.
* **Bibliotecas:**
  * `yfinance`: Coleta de dados históricos de ações.
  * `pandas`: Manipulação e análise de dados.
  * `numpy`: Cálculos numéricos.
  * `matplotlib`: Criação de gráficos.
  * `pyautogui`, `pyperclip`, `webbrowser`: Automação de tarefas e envio de e-mails.

## Próximos Passos
* **Ampliar o período de análise:** Analisar a ação AAPL em um período mais longo.
* **Incorporar outras métricas:** Utilizar outras métricas financeiras para complementar a análise.
* **Comparar com outras ações:** Comparar o desempenho da AAPL com outras ações do setor ou do índice S&P 500.
* **Criar um modelo preditivo:** Desenvolver um modelo para prever os preços futuros da ação.
