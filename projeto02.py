import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker =  input("Digite o codigo da acao desejada: ")

dados = yfinance.Ticker(ticker).history(start = "2020-01-01", end = "2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# Coloquei o meu email de exemplo 
destinatario = "bortoleto355@gmail.com"
assunto = "analise do projeto 2020"

mensagem = f"""
Prezado gestor  

Segue as analises solicitadas da acao {ticker}

Cotacao maxima: R${maxima}
Cotacao minima: R${minima}
valor medio: R${valor_medio}


Qualquer duvida estou a disposicao

att.
"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# Configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar nop botao ESCREVER
pyautogui.click(x=155, y=175)

# digitar o assunto do destinatario e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# clicar no enviar
pyautogui.click(x=1309, y=1025)

print("enviado com sucesso")
