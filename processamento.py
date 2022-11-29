import os
from limpeza import limpar

def processar(arquivo):

    arquivo = open(os.path.abspath(arquivo), "r")
    linhas = arquivo.read().split("\n")
    print("print de teste, as linhas são: ", linhas)
    destino = open(os.path.abspath("result.txt"), "w")
    for linha in linhas:
        linha = limpar(linha)
        destino.write(linha+"\n")

    destino.close

    print("pós limpeza:", linhas)


    arquivo.close()
