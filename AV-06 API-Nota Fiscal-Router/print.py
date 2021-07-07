from Cliente import Cliente
from Item import ItemNotaFiscal
import datetime

class NotaFiscal:
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._itens = []
        self._valorNota = 0.0

    def get_id(self):
        return self._Id
    def get_codigo(self):
        return self._codigo
    def get_cliente(self):
        return self._cliente
    def get_cliente_dict(self):
        return self._cliente.dict()
    def get_data(self):
        return str(self._data)
    def get_data_formatada(self):
        return self.data_formatada()
    def get_itens(self):
        return self._itens
    def get_valor_nota(self):
        return self._valorNota
    def setCliente(self, cliente):
            self._cliente = cliente
    def set_codigo(self, codigo):
        self._codigo = codigo
    def adicionarItem(self, item):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0
        for item in self._itens:
            valor = valor + item.get_valor_item()
        self._valorNota = valor

    def data_formatada(self):
        data_hora_lista = str(self._data).split()
        data_lista = data_hora_lista[0].split('-')
        data_final = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'
        return data_final
    def imprimirNotaFiscal(self):       
        print("+----------------------------------------------------------------------------------------------------------------+")
        print("{:20s} {:>92s}".format('NOTA FISCAL', str(self._data)))
        print("Cliente: " + str(self._cliente._id) + "      " + "Nome: " + self._cliente._nome)
        print("CPF/CNPJ: " + self._cliente._cnpjcpf)
        print("+----------------------------------------------------------------------------------------------------------------+")
        print("ITENS")
        print("+----------------------------------------------------------------------------------------------------------------+")
        print("{:20s} {:20s} {:>29s} {:>20s} {:>20s}".format("Seq", "Descrição", "QTD", "Valor Unit", "Preço"))
        print("{:20s} {:20s} {:>29s} {:>20s} {:>20s}".format("---", "---------", "---", "----------", "-----"))
        for item in self._itens:
                print("{:03d} {:>30s} {:>35d} {:>18.2f} {:>23.2f}".format(item._sequencial, item._descricao, item._quantidade, item._valorUnitario, item._valorItem ))
        print("+----------------------------------------------------------------------------------------------------------------+")
        if len(self._itens) > 0:
            for itemnota in self._itens:
                resultado += '\n\n%s%3s%s' % (itemnota.get_sequencial(), ' ', itemnota.get_descricao())
                resultado += ' ' * (60 - len(itemnota.get_descricao()))
                resultado += '%5d%17.2f%23.2f' % (itemnota.get_quantidade(), itemnota.get_valor_unitario(),
                                                  itemnota.get_valor_item())

        resultado += '\nValor Total: %.2f' % (self._valorNota)

        return resultado

    def dict(self):
        return {'id': self.get_id(),
                'codigo': self.get_codigo(),
                'data': self.get_data(),
                'cliente': self.get_cliente().dict(),
                'itens': [i.dict() for i in self._itens],
                'valor-nota': self.get_valor_nota()
                }