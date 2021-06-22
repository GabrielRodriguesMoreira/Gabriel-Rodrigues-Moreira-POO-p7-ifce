from flask import Flask
from flask_restplus import Api, Resource
from src.cliente import Cliente, cliente
from server.Instance import server

app, api = server.app, server.api


@api.route('/cliente')


class ClientList(Resource):
    def get(self, ):
        return cliente.str()