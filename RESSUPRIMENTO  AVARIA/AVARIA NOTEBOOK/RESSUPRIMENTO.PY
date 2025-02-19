
import pyautogui
import time
import pandas as pd 

x = 0
y = 0 

caminho = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/RESSUPRIMENTO  AVARIA/AVARIA NOTEBOOK/RESSUPRIMENTO.xlsx"
ler = pd.read_excel(caminho)
tabela = pd.DataFrame(ler)
print(tabela)

while True and x < len (tabela):
    ilpn = tabela.iloc[x , y]
    posicao = tabela.iloc[x, y + 1]
    print(ilpn)
    pyautogui.doubleClick(78, 175)
    pyautogui.write("0")
    pyautogui.write(str(ilpn))
    pyautogui.press("enter")
    time.sleep(0.8)
    pyautogui.leftClick(543, 177)
    time.sleep(0.8)
    pyautogui.leftClick(124, 187)
    time.sleep(0.8)
    pyautogui.write(str(posicao))
    time.sleep(1)
    pyautogui.press("enter")
    with pyautogui.hold("ctrl"):
        pyautogui.press("a")
        time.sleep(1)
    pyautogui.hotkey("ctrl" , "a")
    time.sleep(1)
    x = x + 1
    time.sleep(1)