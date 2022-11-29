import os
from limpeza import limpar

def processar(arquivo):

    arquivo = open(os.path.abspath(arquivo), "r")
    linhas = arquivo.read().split("\n")
    print("print de teste, as linhas são: ", linhas)
    
    for linha in linhas:
        linha = limpar(linha)
        print(linha)

    print("pós limpeza:", linhas)


    arquivo.close()
