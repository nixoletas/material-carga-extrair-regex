import re
from functools import total_ordering
from filters.reg import processar_linhas
import PyPDF2
import json
from filters.remove_keywords import descartar

carga_path = './docs/carga.pdf'
output_path = './output/saida.json'

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
        print(text)

        lines = text.split('\n')

        # Filtra as linhas que não precisam ser descartadas
        for line in lines:
            if not descartar(line):
                full_text += line + '\n'

    # Normalizar quebras de linha
    full_text = re.sub(r'\n+', ' ', full_text)

    # Processar o texto acumulado
    resultados = processar_linhas(full_text)

    # Grava os resultados no arquivo JSON no formato de dicionário
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(resultados, output_file, ensure_ascii=False, indent=4)

    print(f"✅")
