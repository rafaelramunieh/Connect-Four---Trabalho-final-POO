from typing import List

class Jogador(): #Define a classe Jogador
    def __init__(self, nome:str, peca:str, tipo:str='humano'): #Método construtor do objeto jogador
        self.nome = nome
        self.peca = peca
        self.tipo = tipo

    def __str__(self):
        """
        Retorna a representação de string legível do objeto Jogador.
        Chamado automaticamente por print() e f-strings.
        """
        return f"{self.nome} ({self.peca})"
