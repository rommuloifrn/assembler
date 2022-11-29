def limpar(linha):

    if ".text" in linha:
        linha = linha.replace(".text", " ")

    if ":" in linha:
        doispontos = linha.index(":")
        linha = linha[doispontos + 1:]

    if "#" in linha:
        linha = linha[ :linha.index("#") ]

    if "," in linha:
        linha = linha.replace(",", "")

    if "$" in linha:
        linha = linha.replace("$", "")
        
    if "    " in linha:
        linha = linha.replace(" ", "")

    return linha


