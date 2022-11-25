def limpar(linha):

    if "." in linha:
        linha = linha.replace(".text", "")

    if ":" in linha:
        doispontos = linha.index(":")
        linha = linha[doispontos + 1:]

    if "#" in linha:
        linha = linha[ :linha.index("#") ]

    #linha = linha.replace(",", " ")
    #linha = linha.replace("$", " ")
    #linha = linha.replace(" ", " ")

    return linha


