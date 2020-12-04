#!/usr/bin/python3

import argparse
import random
import os

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''\
Gerador de senhas em português.
exemplo: cuangares -t 5 -q 5''')
parser.add_argument('-d', action = 'store', dest = 'd', required = False, metavar='[dicionario]',
                    help = 'Dicionario customizavel.')
parser.add_argument('-f', action = 'store', dest = 'f', default=4, required = False, metavar='[formato]',
                    help = 'Formato da senha 1:[A-Z] 2:[A-Za-z] 3:[A-Za-z0-9] 4:[ascii printable] 5:[dictionary]')
parser.add_argument('-t', action = 'store', dest = 't', metavar='[tamanho]',
                    default = 'Hello, world!', required = True,
                    help = 'Tamanho da senha.')
parser.add_argument('-q', action = 'store', dest = 'q', required = True, metavar='[quantidade]',
                    help = 'Quantidade de senhas.')

arguments = parser.parse_args()
escolha = int(arguments.f)
quant = int(arguments.q)
tam = int(arguments.t)

arq = "dicionario.txt"
senha = ''
alfabeto1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfabeto3 = ['0','1','2','3','4','5','6','7','8','9','a','b','c',
             'd','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','A','B','C',
             'D','E','F','G','H','I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']
alfabeto4 = ['0','1','2','3','4','5','6','7','8','9','a','b','c',
             'd','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','A','B','C',
             'D','E','F','G','H','I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z','!','#','$',
             '%','&',':',';','?','@']

def limpar_terminal():
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def ler_dic(arquivo):
    dicionario = open(arquivo, "r")
    global palavras
    palavras = dicionario.read().split('\n')
    dicionario.close()
    
def gerarDic(arquivo, quant, tam):
    print("----------AQUI COMEÇAM AS SENHAS----------")
    for i in range(quant):
        senha = ''.join(random.sample(palavras, tam))
        print(senha)
    print("----------AQUI TERMINAM AS SENHAS----------")

def gerarRand(quant, tam, alfabeto):
    print("----------AQUI COMEÇAM AS SENHAS----------")
    for i in range(quant):
        senha = ''.join(random.sample(alfabeto, tam))
        print(senha)
    print("----------AQUI TERMINAM AS SENHAS----------")

def main(escolha, quant, tam):
    if(escolha == 5):
        tam = int(input('Quantidade de palavras: '))

    if(escolha == 1):
        gerarRand(quant, tam, alfabeto1)
    elif(escolha == 2):
        gerarRand(quant, tam, alfabeto2)
    elif(escolha == 3):
        gerarRand(quant, tam, alfabeto3)
    elif(escolha == 4):
        gerarRand(quant, tam, alfabeto4)
    elif(escolha == 5):
        ler_dic(arq)
        gerarDic(arq, quant, tam)
    else:
        print('Escolha inválida')

main(escolha, quant, tam)

