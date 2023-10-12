from interface import * #Importa funções do arquivo "interface.py"
from random import choice #Importa função "choice" da biblioteca "random"
from time import sleep

from leiaInt_1 import leiaInt #Importa função "sleep" da biblioteca "time"

senha = [] #Lista da senha

#Input da quantidade de senhas
def quant_senhas():
    quant = leiaInt("Quantidade: ")
    return quant

#Input do tamanho das senhas
def tam_senhas():
    tam = leiaInt("Tamanho: ")
    return tam

#Gerador de senhas
def gerador_senhas(quant, tam)
    cabecalho("GERANDO SENHAS...")
    sleep(1)

    strings = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")

    for senha_gerada in range(0, int(quant)):
        for string in range(0, int(tam)):
            senha.append(choice(strings))

        for caracter in senha:
            print(caracter, end="")

        print("")
        senha.clear()
        sleep(1)


