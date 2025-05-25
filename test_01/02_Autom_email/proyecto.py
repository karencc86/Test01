import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digita el código de la acción: ")
data = yfinance.Ticker(ticker).history("6mo")
cierre = data.Close

maxima = round(cierre.max(), 2)
minima = round(cierre.min(), 2)
valor_medio = round(cierre.mean(), 2)

destinatario = "xxxxx@gmail.com"
asunto = "Análisis acciones últimos 6 meses"

# Hacer un f string para insertar las variables
mensaje = f"""
Hola 

Acá te envío el análisis de los últimos 6 meses de : {ticker}

Cotización máxima: USD {maxima}
Cotización mínima: USD {minima}
Valor medio: USD {valor_medio}

Cualquier cosa me cuentas.
"""
# Abrir el navegador para ir a Gmail
webbrowser.open("https://mail.google.com/mail/u/1/?ogbl#inbox")
time.sleep(5)


pyautogui.PAUSE = 5

# Click en el botón Redactar
pyautogui.click(2510, 270)

# Escribir el destinatario
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v") #Para efectuar comandos del teclado
pyautogui.hotkey("tab")

# Escribir el asunto
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Escribir el mensaje

pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")

# Click en el botón de Enviar
pyautogui.click(4015, 1255)

# Cerrar Gmail
pyautogui.hotkey("ctrl", "f4")
