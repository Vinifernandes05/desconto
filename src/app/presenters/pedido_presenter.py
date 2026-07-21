from desconto_app.src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

# Classe responsável por apresentar os dados de saída do processo de criação de um pedido, formatando-os em um dicionário ou lista de dicionários para facilitar a visualização e o consumo das informações.
class PedidoPresenter:
    def apresentar(self, output_dto: CriarPedidoOutputDTO) -> dict:
        return {
            "cliente": output_dto.cliente,
            "valor_original": output_dto.valor_original,
            "valor_desconto": output_dto.valor_desconto,
            "valor_final": output_dto.valor_final,
            "tipo_desconto": output_dto.tipo_desconto
        }

# Apresenta uma lista de pedidos formatados, convertendo cada DTO de saída em um dicionário e retornando uma lista desses dicionários.
    def apresentar_lista(self, output_dtos: list[CriarPedidoOutputDTO]) -> list[dict]:
        lista_formatada = []

        for output_dto in output_dtos:
            pedido_formatado = self.apresentar(output_dto)
            lista_formatada.append(pedido_formatado)

        return lista_formatada