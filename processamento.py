import os
from limpeza import limpar

def processar(arquivo):

    arquivo = open(os.path.abspath(arquivo), "r")
    linhas = arquivo.read().split("\n")
    for linha in linhas:
        limpar(linha)

    print("pré-limpeza:", linhas)
    linhas = limpar(linhas)
    print("pós-limpeza:", linhas)
    

    arquivo.close()
