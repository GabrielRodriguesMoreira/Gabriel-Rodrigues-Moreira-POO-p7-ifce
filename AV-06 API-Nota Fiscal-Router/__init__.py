import json
from flask import resposta

def objeto_json(objeto):
    if isinstance(objeto, list):
        json_final = []
        for objeto in objeto:
            json_final.append(objeto.dict())
        return json_final
    else:
        return objeto.dict()


def resposta(status, nome, conteudo, mensagem=''):
    body = {nome: conteudo}
    if mensagem:
        body["mensagem"] = mensagem
    return resposta(json.dumps(body), status=status, mimetype="api/json")

def selecionarobjeto(lista, id_objeto):
    for o in lista:
        if o.get_id() == id_objeto:
            return o