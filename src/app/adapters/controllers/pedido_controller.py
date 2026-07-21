from desconto_app.src.app.use_cases.criar_pedido import CriarPedido
from desconto_app.src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from desconto_app.src.app.presenters.pedido_presenter import PedidoPresenter

# Controle de pedidos, responsável por receber as requisições e interagir com o caso de uso e o apresentador.
class PedidoController: 
    def __init__(self, criar_pedido_use_case: CriarPedido, presenter: PedidoPresenter): 
        self.criar_pedido_use_case = criar_pedido_use_case
        self.presenter = presenter 

# Método para criar um pedido, recebe os parâmetros, cria o DTO de entrada, executa o caso de uso e retorna a resposta formatada.
    def criar_pedido(self, cliente: str, valor_original: float, tipo_desconto: str):
        input_dto = CriarPedidoInputDTO(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto
        )

        output_dto = self.criar_pedido_use_case.executar(input_dto)
        return self.presenter.apresentar(output_dto)
    
# Método para listar todos os pedidos, executa o caso de uso e retorna a resposta formatada. 
    def listar_pedidos(self):
        output_dtos = self.criar_pedido_use_case.listar_pedidos()
        return self.presenter.apresentar_lista(output_dtos)