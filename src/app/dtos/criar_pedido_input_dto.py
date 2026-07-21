# Classe DTO (Data Transfer Object) para criar um pedido.
class CriarPedidoInputDTO:
    def __init__(self, cliente: str, valor_original:float, tipo_desconto: str):
        self.cliente = cliente
        self.valor_original = valor_original
        self.tipo_desconto = tipo_desconto