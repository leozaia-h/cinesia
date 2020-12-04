# cuangares
gerador de senhas

chmod +x cuangares.py

./cuangares -h
  usage: cuangares.py [-h] [-d [dicionario]] [-f [formato]] -t [tamanho] -q [quantidade]

  Gerador de senhas em português.
  exemplo: cuangares -t 5 -q 5

  optional arguments:
    -h, --help       show this help message and exit
    -d [dicionario]  Dicionario customizavel.
    -f [formato]     Formato da senha 1:[A-Z] 2:[A-Za-z] 3:[A-Za-z0-9] 4:[ascii printable] 5:[dictionary]
    -t [tamanho]     Tamanho da senha.
    -q [quantidade]  Quantidade de senhas.
