from desconto_app.src.app.entities.pedido import Pedido
from desconto_app.src.app.gateways.pedido_gateway import IPedidoGateway
from desconto_app.src.app.frameworks.database.memory_database import MemoryDatabase

# Implementação concreta da interface IPedidoGateway que utiliza um banco de dados em memória para armazenar e recuperar objetos Pedido. Ele fornece métodos para salvar um Pedido, juntamente com seu tipo de desconto associado, e para listar todos os Pedidos armazenados.
class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatabase):
        self.database = database

# O método salvar adiciona um novo pedido ao banco de dados em memória, armazenando o objeto Pedido e o tipo de desconto associado. O método listar retorna uma lista de todos os pedidos armazenados no banco de dados em memória.
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        self.database.pedidos.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

# O método listar retorna uma lista de todos os pedidos armazenados no banco de dados em memória.
    def listar(self) -> list[Pedido]:
        return self.database.pedidos