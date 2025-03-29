import time
import pyautogui
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')#abre o chrome
time.sleep(2)


pyautogui.click(x=955, y=599) #clica no icone com o meu nome

pyautogui.click(x=780, y=84)#clica na barra de pesquisamAYARA   yasmin  

pyautogui.click(x=780, y=84)

time.sleep(2)
pyautogui.write('https://app.tagplus.com.br/f96r3dy4/')#url para o site

time.sleep(0.5)
pyautogui.press('enter')#entramos no site

time.sleep(3)

pyautogui.click(x=1285, y=394)
time.sleep(1)

pyautogui.write('Mayara')
pyautogui.press('tab')
pyautogui.write('YASMIN')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(4)
pyautogui.click(x=31, y=514)#aqui eu clico no menu para entrar na aba de relatorios 
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=306, y=381)#clico para o relatorio comercial
pyautogui.click(x=662, y=295)
pyautogui.press('enter')#abre uma nova janela 
time.sleep(2)
pyautogui.click(x=592, y=829) #faço as configurações necessarias 
pyautogui.click(x=591, y=695)
time.sleep(2)
 
pyautogui.click(x=375, y=205)#abro para gerar relatorios
time.sleep(4)
pyautogui.click(x=1170, y=199)#clico para selecionar as colunas
time.sleep(2)
pyautogui.click(x=1256, y=484)#desmarca a opção cliente
pyautogui.click(x=1253, y=560)#desmarca a opção data considerada
pyautogui.click(x=1270, y=630)#marca a opção data de criação
pyautogui.click(x=1248, y=658)#marca a opção desconto
pyautogui.click(x=1466, y=338)#seleção de colunas
pyautogui.scroll(-1100) #arrasca o mouser

pyautogui.click(x=1173, y=336)#seleção de colunas
pyautogui.click(x=1258, y=642)#seleção de colunas
pyautogui.click(x=1192, y=739)#seleção de colunas
pyautogui.click(x=759, y=202)#gerar planilha
time.sleep(2)
pyautogui.click(x=215, y=350)#clico para opção de downlod
pyautogui.click(x=843, y=556)#salvar
time.sleep(3)
pyautogui.click(x=1803, y=90) #icone de download
pyautogui.click(x=1803, y=90)  #icone de download

time.sleep(1) 

pyautogui.click(x=1640, y=182)#clico na pasta excel
pyautogui.click(x=1640, y=182)

time.sleep(2)

pyautogui.click(x=1485, y=100)#habilitar edição


time.sleep(0.5)  
pyautogui.click(x=5, y=290)#clica na primeira celula do excel
time.sleep(0.5) 


pyautogui.dragTo(5, 350, duration=0.5)#arrasta o mouser

time.sleep(0.5)

pyautogui.click(x=16, y=342,button='right')#clica no botão direito do mouse
pyautogui.click(x=100, y=573)#apaga 

pyautogui.click(x=327, y=341)#celula aleatoria

pyautogui.hotkey('ctrl', 't')#seleciona toda a tabela

pyautogui.click(x=965, y=282)#clica no incone de alerta

pyautogui.click(x=1006, y=342)#clica para transformar em numero

time.sleep(1)

pyautogui.click(x=1055, y=108)
pyautogui.click(x=1010, y=258)













