def descartar(linha):
    # Lista de palavras-chave que identificam cabeçalhos ou rodapés
    palavras_chave = [
        "MINISTÉRIO", "EXÉRCITO", "BRASILEIRO", "Página",
        "9º BATALHÃO DE COMUNICAÇÕES E GUERRA ELETRÔNICA",
        "RELAÇÃO DE MATERIAL CARGA DA DEPENDÊNCIA",
        "MATERIAL PERMANENTE", "Nr Ficha", "Nr Patrimônio",
        "Cod Mat", "Nome material", "Nr Lote Mat", "Ano Lote",
        "Numero Mat.", "Numero  Comp.", "Nr Série Mat.",
        "Nr Série Comp.", "Conta Contábil", "Valor Patr",
        "Qtde Componente", "Nome componente", "Cod Mat Comp",
        "(*) Observação do cadastro inicial",
        "(**) Observação do último movimento",
        "Bol de  Inclusão  em  Carga", "Dt Incl Carga",
        "Nr Registro Vtr (EB)", "Placa", "Acervo",
        "Atributos de Patrimônio","Nr Ficha, Nr Patrimônio, Cod Mat, Nome material, Nr Lote Mat, Ano Lote, Numero Mat., Numero  Comp., Nr Série Mat., Nr Série Comp., Conta Contábil, Valor Patr, Qtde Componente, Nome componente, Cod Mat Comp, (*) Observação do cadastro inicial, (**) Observação do último movimento, Bol de  Inclusão  em  Carga, Dt Incl Carga, Nr Registro Vtr (EB), Placa, Acervo, Atributos de Patrimônio",
        "Relação emitida pelo SISCOFIS OM - Usuário : IDS0305618670 / JOKOBSON - Data de emissão : terça-feira, 6 de agosto de 2024",
        "Valor total dos materiais de uso duradouro da dependência:    Número total de materiais de uso duradouro da dependência:    74",
        "FABIO", "HENRIQUE", "FREITAS", "DE", "OLIVEIRA", "2º Ten"
    ]

    # Verifica se alguma palavra-chave está presente na linha
    for palavra in palavras_chave:
        linha = linha.replace(palavra, '')

    return linha.strip() == ''