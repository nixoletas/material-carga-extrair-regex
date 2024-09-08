from filters.reg import processar_linhas
import PyPDF2
import csv
import re
from filters.remove_keywords import descartar

carga_path = './docs/carga.pdf'
csv_output_path = './output/saida.csv'

# Processamento do PDF e saída em JSON formatado
with open(carga_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pages = len(pdf_reader.pages)

    full_text = ""

    # Extrair o texto do PDF
    i = 1
    for page in range(pages):
        props = pdf_reader.pages[page]
        text = props.extract_text()

        lines = text.split('\n')

        # Filtra as linhas que não precisam ser descartadas
        for line in lines:
            if not descartar(line):
                full_text += line + '\n'

    # Normalizar quebras de linha
    full_text = re.sub(r'\n+', ' ', full_text)

    # Processar o texto acumulado
    resultado_regex = processar_linhas(full_text)

    # Grava os resultados no arquivo JSON no formato de dicionário
    with open(csv_output_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = [
            "patr",
            "cod_mat",
            "component",
            "valor",
            "serie",
            "nr_mat",
            "descricao",
            "obs",
            "movimento",
            "boletim",
            "data_inclusao",
            "status",
            "local"
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Escreve o cabeçalho no CSV
        writer.writeheader()

        # Escreve as linhas no CSV
        for resultado in resultado_regex:
            writer.writerow(resultado)

    print(f"✅")
