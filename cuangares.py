import random
import os

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

def main():
    limpar_terminal()
    while(True):
        print("                            ,--.                                              ")
        print("  ,----..     ,---,       ,--.'|    ,---,.  .--.--.      ,---,   ,---,        ")
        print(" /   /   \ ,`--.' |   ,--,:  : |  ,'  .' | /  /    '. ,`--.' |  '  .' \       ")
        print("|   :     :|   :  :,`--.'`|  ' :,---.'   ||  :  /`. / |   :  : /  ;    '.     ")
        print(".   |  ;. /:   |  '|   :  :  | ||   |   .';  |  |--`  :   |  ':  :       \    ")
        print(".   ; /--` |   :  |:   |   \ | ::   :  |-,|  :  ;_    |   :  |:  |   /\   \   ")
        print(";   | ;    '   '  ;|   : '  '; |:   |  ;/| \  \    `. '   '  ;|  :  ' ;.   :  ")
        print("|   : |    |   |  |'   ' ;.    ;|   :   .'  `----.   \|   |  ||  |  ;/  \   \ ")
        print(".   | '___ '   :  ;|   | | \   ||   |  |-,  __ \  \  |'   :  ;'  :  | \  \ ,' ")
        print("'   ; : .'||   |  ''   : |  ; .''   :  ;/| /  /`--'  /|   |  '|  |  '  '--'   ")
        print("'   | '/  :'   :  ||   | '`--'  |   |    \'--'.     / '   :  ||  :  :         ")
        print("|   :    / ;   |.' '   : |      |   :   .'  `--'---'  ;   |.' |  | ,'         ")
        print(" \   \ .'  '---'   ;   |.'      |   | ,'              '---'   `--''           ")
        print("  `---`            '---'        `----'                                   v1.0 ")

        print('Escolha um formato:\
               \n1) ABDC\
               \n2) ABcd\
               \n3) Abc1\
               \n4) Ab3@\
               \n5) Dicionario PT\
               \n9) Sair')

        escolha = int(input(': '))
        quant = int(input('Quantidade de senhas: '))
        if(escolha == 5):
            tam = int(input('Quantidade de palavras: '))
        else:
            tam = int(input('Quantidade de letras: '))

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
        elif(escolha == 9):
            exit()
        else:
            print('Escolha inválida')

        os.system("PAUSE")

main()

