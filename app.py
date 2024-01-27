import pyautogui
from time import sleep

# 1 - Fixar local de user e escrever
pyautogui.click(725,389,duration=0)
pyautogui.write('Bruno')
# 2 - Fixar local de senha e escrever
pyautogui.click(687,415,duration=1)
pyautogui.write('1234')
# 3 - Clicar em iniciar
pyautogui.click(598,441,duration=1)

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # Digitar nome produto
        pyautogui.click(432,364)
        pyautogui.write(produto)
        # Digitar nome produto
        pyautogui.click(429,399)
        pyautogui.write(quantidade)
        # Digitar nome produto
        pyautogui.click(439,429)
        pyautogui.write(preco)
        # Registrar
        pyautogui.click(326,578)
