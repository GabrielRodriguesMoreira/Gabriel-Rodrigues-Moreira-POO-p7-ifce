"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
from datetime       import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente
        self._data=datetime.today().strftime('%d/%m/%Y')  
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
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
    
    