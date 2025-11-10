from typing import List

class Jogador():
    def __init__(self, nome:str, peca:str, tipo:str='humano'):
        self.nome = nome
        self.peca = peca
        self.tipo = tipo
    
    def obter_jogada(self, tabuleiro:List[List[str]]):
        pass