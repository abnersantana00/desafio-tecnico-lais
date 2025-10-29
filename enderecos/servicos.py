import requests
VIA_CEP_URL = "https://viacep.com.br/ws/{cep}/json/"

def consulta_viacep(cep: str) -> dict:
    url = VIA_CEP_URL.format(cep=cep_fmt.replace("-", ""))
    resp = request.get(url, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    if "erro" in data:
        raise ValueError("CEP não encontrado")
    return {
        "cep": data.get("cep"),
        "logradouro": data.get("logradouro"),
        "complemento": data.get("complemento"),
        "unidade": data.get("unidade"),
        "bairro": data.get("bairro"),
        "localidade": data.get("localidade"),
        "uf": data.get("uf"),
        "regiao": data.get("regiao"),
        "ibge": data.get("ibge"),
        "gia": data.get("gia"),
        "ddd": data.get("ddd"),
        "siafi": data.get("siafi"),
    }
 