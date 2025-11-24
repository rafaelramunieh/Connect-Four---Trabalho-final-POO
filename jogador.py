from typing import List

class Jogador(): #Define a classe Jogador
    def __init__(self, nome:str, peca:str, tipo:str='humano'): #Método construtor do objeto jogador
        self.nome = nome
        self.peca = peca
        self.tipo = tipo
