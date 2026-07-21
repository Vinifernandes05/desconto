from desconto_app.src.app.entities.desconto import IDesconto

# Classe que representa um pedido, contendo informações sobre o cliente, valor original e o tipo de desconto aplicado.
class Pedido:
    def __init__(self, cliente: str, valor_original: float, desconto: IDesconto):
        self.cliente = cliente
        self.valor_original = valor_original
        self.desconto = desconto

# calcula o valor do desconto aplicando a estratégia de desconto fornecida.
    def valor_desconto(self) -> float:
        return self.desconto.calcular(self.valor_original)

# calcula o valor final do pedido subtraindo o valor do desconto do valor original.
    def valor_final(self) -> float:
        return self.valor_original - self.valor_desconto()