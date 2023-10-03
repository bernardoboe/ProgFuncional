class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def cadastrar_produto(self):
        return self.nome, self.preco, self.estoque
    
    def atualizar_produto(self):
        return self.nome, self.preco, self.estoque

class Item(Produto):
    def __init__(self, nome, preco, estoque, quantidade):
        super().__init__(nome, preco, estoque)
        self.quantidade = quantidade

        def qtd_item(self):
            return self.quantidade


class Pedido:
    def __init__(self, Cliente, forma_pagamento):
        
        self.Cliente = Cliente()
        self.forma_pagamento = forma_pagamento
        
    def cadastrar_pedido(self):
        return self.Cliente, self.forma_pagamento
    
    def adicionar_item(self, Item):
        return Item
    
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def cadastrar_cliente(self):
        return self.nome, self.cpf

    def atualizar_cliente(self):
        return self.nome, self.cpf