# Classe responsável por gerenciar a conexão com o banco de dados, armazenando os pedidos criados em memória.
class MemoryDatabase:
    def __init__(self):
        self.pedidos = []