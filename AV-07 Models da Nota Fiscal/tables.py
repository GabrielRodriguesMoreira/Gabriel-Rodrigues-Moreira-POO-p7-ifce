from app import db

class Clientes(db.Model):
        __tablename__='Cliente'

        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String, unique=True)
        codigo = db.Column(db.Integer)
        cnpjcpf = db.Column(db.String, unique=True)
        tipo = db.Column(db.String)

        def __init__(self, nome, codigo, cnpjcpf, tipo):
                self.nome = nome
                self.codigo = codigo
                self.cnpjcpf = cnpjcpf
                self.tipo = tipo
                
        def __repr__(self):
            return "<nome %r>" %self.nome


class Produtos(db.Model):
    __tablename__ = "Produtos"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.Text)
    valor_unitario = db.Column(db.Float)

    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor

        def __repr__(self):
            return "<codigo %r>" %self.codigo


class Itens(db.Model):
        __tablename__='Itens'
        id = db.Column(db.Integer, primary_key=True)
        sequencial = db.Column(db.Integer)
        quantidade = db.Column(db.Integer)
        produto_id = db.Column(db.Integer, db.ForeignKey('Produtos.id'))

        def __init__(self, sequencial, quantidade, produto_id):
                self.sequencial = sequencial
                self.quantidade = quantidade
                self.produto_id = produto_id