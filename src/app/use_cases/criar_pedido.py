from desconto_app.src.app.entities.pedido import Pedido
from desconto_app.src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from desconto_app.src.app.gateways.pedido_gateway import IPedidoGateway
from desconto_app.src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from desconto_app.src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

# Use case responsável por criar um pedido, aplicando o desconto apropriado com base no tipo de desconto fornecido e interagindo com o gateway de pedidos para salvar e listar os pedidos.
class CriarPedido:
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

# Executa o processo de criação de um pedido, determinando o tipo de desconto a ser aplicado, criando o pedido e salvando-o através do gateway de pedidos. Retorna um DTO de saída contendo as informações do pedido criado.
    def executar(self, input_dto: CriarPedidoInputDTO) -> CriarPedidoOutputDTO:
        tipo_desconto = input_dto.tipo_desconto.lower().strip()
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")
        
        pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
        self.pedido_gateway.salvar(pedido, tipo_desconto)

        return CriarPedidoOutputDTO(
            cliente=input_dto.cliente,
            valor_original=input_dto.valor_original,
            valor_desconto=pedido.valor_desconto,
            valor_final=pedido.valor_final,
            tipo_desconto=tipo_desconto
        )

# Lista todos os pedidos salvos, retornando uma lista de DTOs de saída contendo as informações de cada pedido.
    def listar_pedidos(self) -> list[CriarPedidoOutputDTO]:
        pedidos = self.pedido_gateway.listar()
        lista_dto = []
        for registro in pedidos:
            pedido = registro["pedido"]
            dto = CriarPedidoOutputDTO(
                cliente=pedido.cliente,
                valor_original=pedido.valor_original,
                valor_desconto=pedido.valor_desconto(),
                valor_final=pedido.valor_final(),
                tipo_desconto=registro["tipo_desconto"]
            )
            lista_dto.append(dto)
        return lista_dto