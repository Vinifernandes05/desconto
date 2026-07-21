from desconto_app.src.app.entities.pedido import Pedido
    
# Classe responsável por gerenciar os pedidos, incluindo a adição de novos pedidos e o processamento dos pedidos existentes, interagindo com o repositório de pedidos para armazenar e recuperar informações.
class PedidoService:

    def __init__(self, repository):
        self.repository = repository

# Adiciona um novo pedido ao repositório, utilizando o método de adição do repositório para armazenar o pedido criado.
    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

# Processa os pedidos existentes, listando cada pedido e exibindo informações relevantes, como o cliente e o valor final do pedido após a aplicação do desconto.
    def processar_pedidos(self):
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")