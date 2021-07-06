from flask import Flask, request
from flask_restplus import Api, Resource
from __init__ import objeto_json, resposta, selecionarobjeto
from instance import Server
from Cliente import Cliente
from Produto import Produto
from nota import NotaFiscal
from Item import ItemNotaFiscal

app = Server.app
api = Server.api

cliente1 = Cliente(1, "Jose Maria", 100, '200.100.345-34', "PESSOA_FISICA")
produto1 = Produto(0, 100, 'Arroz 101', 5.5)
nota_fiscal1 = NotaFiscal(0, 100, cliente1)
item1 = ItemNotaFiscal(0, 1, 2, produto1)

clientes_db = [cliente1]
products_db = [produto1]
nf_db = [nota_fiscal1]
itens_db = [item1]

class Clientes(Api, Resource):
    @api.route('/clients')
    def get(self):
        clientes_json = objeto_json(clientes_db)
        return resposta, 200, clientes_json

    @api.route('/cliente/<int:id_cliente>')
    def get(self, id_cliente):
        client = selecionarobjeto(clientes_db, id_cliente)
        cliente_json = objeto_json(client)
        return resposta, 200, cliente_json

    @api.route('/cliente')
    def post(self):
        body = request.json
        cliente = Cliente(clientes_db[-1].get_id(), body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
        clientes_db.append(cliente)
        cliente_json = objeto_json(cliente)
        return resposta, 200, cliente_json

    @api.route('/cliente/<int:id_cliente>')
    def put(self, id_cliente):
        body = request.json
        cliente = selecionarobjeto(clientes_db, id_cliente)
        cliente.set_nome(body['nome'])
        cliente.set_codigo(body['codigo'])
        cliente.set_cnpjcpf(body['cpf'])
        cliente_json = objeto_json(cliente)
        return resposta, 200, cliente_json


    @api.route('/cliente/<int:id_cliente>')
    def delete(self, id_cliente):

        cliente = selecionarobjeto(clientes_db, id_cliente)
        clientes_db.remove(cliente)
        return resposta, 200


class Itens(Api, Resource):
    @api.route('/itensnf/<int:id_nota>')
    def get(self, id_nota):
        itens_nf = selecionarobjeto(nf_db, id_nota).get_itens()
        itens_json = objeto_json(itens_nf)
        return resposta, 200, itens_json


    @api.route('/itemnf/<int:id_item>')
    def get(self, id_item):
        item = selecionarobjeto(itens_db, id_item)
        item_json = objeto_json(item)
        return resposta, 200, item_json

    @api.route('/itemnf')
    def post(self):
        body = request.json
        produto = selecionarobjeto(products_db, body['produto'])
        item = ItemNotaFiscal(itens_db[-1].get_id() + 1, body['sequencial'], body['quantidade'], produto)
        itens_db.append(item)
        item_json = objeto_json(item)
        return resposta, 200, item_json

    @api.route('/itemnf/<int:id_item>')
    def put(self, id_item):
        body = request.json
        item = selecionarobjeto(itens_db, id_item)
        item.set_sequencial(body['sequencial'])
        item.set_quantidade(body['quantidade'])

        item_json = objeto_json(item)
        return resposta, 200, item_json

    @api.route('/itemnf/<int:id_item>')
    def delete(self, id_item):
        item = selecionarobjeto(itens_db, id_item)
        itens_db.remove(item)
        item_json = objeto_json(item)
        return resposta, 200, item_json


class Notas(Api, Resource):
    @api.route('/notasfiscais')
    def get(self):
        notas_json = objeto_json(nf_db)
        return resposta, 200, notas_json

    @api.route('/notafiscal/<int:id_nota>')
    def get(self, id_nota):
        nota = selecionarobjeto(nf_db, id_nota)
        nota_json = objeto_json(nota)
        return resposta, 200, nota_json


    @api.route('/notafiscal')
    def post(self):
        body = request.json
        cliente = selecionarobjeto(clientes_db, body['cliente'])
        nota = NotaFiscal(nf_db[-1].get_id(), body['codigo'], cliente)
        nf_db.append(nota)
        nota_json = objeto_json(nota)
        return resposta, 201, 'nota', nota_json

    @api.route('/notafiscal/<int:id_nota>')
    def put(self, id_nota):
        body = request.json
        nota = selecionarobjeto(nf_db, id_nota)
        cliente = selecionarobjeto(clientes_db, body['cliente'])
        nota.set_codigo(body['codigo'])
        nota.setCliente(cliente)
        nota_json = objeto_json(nota)
        return resposta, 200, 'nota', nota_json

    @api.route('/notafiscal/<int:id_nota>')
    def delete(self, id_nota):
        nota = selecionarobjeto(nf_db, id_nota)
        nf_db.remove(nota)
        nota_json = objeto_json(nota)
        return resposta, 200, nota_json

    @api.route('/calculanf/<int:id_nota>')
    def get(self, id_nota):
        nota = selecionarobjeto(nf_db, id_nota)
        nota.calcularNotaFiscal()

        nota_json = objeto_json(nota)
        return resposta, 200, nota_json

    @api.route('/imprimenf/<int:id_nota>')
    def get(self, id_nota):
        nota = selecionarobjeto(nf_db, id_nota)
        impressao = nota.imprimirNotaFiscal()
        return resposta, 200, impressao

class Produtos(Api, Resource):
    @api.route('/produtos')
    def get(self):
        protudos_json = objeto_json(products_db)
        return resposta, 200, protudos_json

    @api.route('/produto/<int:id_produto>')
    def get(self, id_produto):
        produto = selecionarobjeto(products_db, id_produto)
        produto_json = objeto_json(produto)
        return resposta, 200, 'produto', produto_json


    @app.route('/produto')
    def post(self):
        body = request.json
        produto = Produto(products_db[-1].get_id() + 1, body['codigo'], body['descricao'], body['valor-unitario'])
        products_db.append(produto)
        produto_json = objeto_json(produto)
        return resposta, 201, 'produto', produto_json

    @app.route('/produto/<int:id_produto>')
    def put(self, id_produto):
        body = request.json
        produto = selecionarobjeto(products_db, id_produto)
        produto.set_codigo(body['codigo'])
        produto.set_descricao(body['descricao'])
        produto.set_valor_unitario(body['valor-unitario'])
        produto_json = objeto_json(produto)
        return resposta, 200, produto_json

    @api.route('/produto/<int:id_produto>')
    def delete(self, id_produto):
        produto = selecionarobjeto(products_db, id_produto)
        products_db.remove(produto)

        produto_json = objeto_json(produto)
        return resposta, 200, 'produto', produto_json