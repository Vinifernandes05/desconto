import abc
from desconto_app.src.app.entities.pedido import Pedido

# Classe abstrata que define a interface para o gateway de pedidos, especificando os métodos que devem ser implementados para salvar e listar pedidos.
class IPedidoGateway(abc.ABC):
        @abc.abstractmethod
        def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
            pass
    
        @abc.abstractmethod
        def listar(self) -> list[Pedido]:
            pass

    
