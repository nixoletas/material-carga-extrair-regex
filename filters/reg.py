import re

def processar_linhas(texto):

    campos = re.compile(
        r'(\d{15})\s\s+(\d\S+)\s\s(\d\S+)\s\s(\d\S+)\s\s([a-zA-Z0-9]\S+)\s\s([a-zA-Z0-9]{1,}\s{2}){3}([^[^(*)]*)\(\*\)(.*?)\(\*\*\)(.*?)BADM\s+(Nr+\s+[0-9]{3},\sde\s\d{1,2}/\d{1,2}/\d{4})\s\s+(\d{1,2}/\d{1,2}/\d{4})', re.DOTALL)

    camposfind = campos.findall(texto)

    resultados = []

    for match in camposfind:
        patr, cod_mat, component, valor, serie, nr_mat, descricao, obs, movimento, boletim, data_inclusao = match

        # Criando um dicionário com os dados organizados
        linha_formatada = {
            "patr": patr,
            "cod_mat": cod_mat,
            "component": component,
            "valor": valor,
            "serie": serie,
            "nr_mat": nr_mat,
            "descricao": descricao,
            "obs": obs,
            "movimento": movimento,
            "boletim": "BADM " + boletim,
            "data_inclusao": data_inclusao,
            "status": "DISPONIVEL",
            "local": "STI"
        }

        resultados.append(linha_formatada)

    return resultados