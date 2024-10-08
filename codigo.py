# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# importando bibliotecas
import pyautogui        # automatizacao
import time             # tempo 
import pandas  as pd    # trabalhar com base de dados

"""
pyautogui.write -> escrever um texto
pyautogui.click -> clicar com o mouse
pyautogui.press -> apertar uma tecla
pyautogui.hotkey -> apertar um atalho de teclado
pyautogui.PAUSE -> adiciona tempo para proxima execucao
pyautogui.position -> mostra posicao do mouse

"""

# Definir um intervalo para execucao de cada comando
pyautogui.PAUSE = 0.5

# abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(3)

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(str(link))
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=416, y=390)

#escrever email
pyautogui.write("angelo-marcos")
# passando pro próximo campo
pyautogui.press("tab")
# escrever senha
pyautogui.write("senha")
pyautogui.press("enter")
# Aguardar carregamento da pagina
time.sleep(2)

# Passo 3: Importar a base de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv") # ler o csv
print(tabela) # imprimir o csv

# Passo 4: Cadastrar um produto
pyautogui.click(x=438, y=281)

# para cada linha da minha tabela
for row in tabela.index:
    # selecionar o 1o campo
    pyautogui.click(x=438, y=281)

    # converter dados da variavel em string = str()

    # codigo
    codigo = tabela.loc[row, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[row, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[row, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[row, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[row, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[row, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    # nan = Not a Number = Null
    obs = tabela.loc[row, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar no botao enviar
    pyautogui.press("enter")

    # voltar para o topo da pagina
    pyautogui.press("home")
# Passo 5: Repetir o processo de cadastro até o fim