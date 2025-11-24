
class Tabuleiro(): #Declara a classe do tabuleiro
    def __init__(self) -> None: 
        self.NUM_LINHAS = 6 #Determina o número de linhas do tabuleiro
        self.NUM_COLUNAS = 7 #Determina o número de colunas do tabuleiro
        self.PECA_VAZIA = '.' #Determina o caractere que representa os espaços vazios do tabuleiro
        self.tabuleiro = [ #Inicia a matriz do tabuleiro 
            [self.PECA_VAZIA for _ in range(self.NUM_COLUNAS)] 
            for _ in range(self.NUM_LINHAS)
        ]
    def obter_linha_livre(self, coluna: int) -> int: #Método que recebe o índice da coluna e retorna o índice da linha vazia mais baixa
        for linha in range(self.NUM_LINHAS - 1, -1, -1):
            
            if self.tabuleiro[linha][coluna] == self.PECA_VAZIA:
                return linha
        
        return -1
    
    def tabuleiro_cheio(self) -> bool: #Método que verifica se todas as colunas estão cheias
        linha_topo = self.tabuleiro[0]
        for i in linha_topo:
            if i == self.PECA_VAZIA:
                return False    
        return True

    
    def mostrar_tabuleiro(self): #Mostra o tabuleiro na tela e suas devidas coordenadas
        CANTO = "🪤"
        print("\n  0 1 2 3 4 5 6")
        print(f" {CANTO}-------------{CANTO}")
        
        for linha in self.tabuleiro:
            print(f"| {' '.join(linha)} |") 
            
        print(f" {CANTO}-------------{CANTO}")


    def fazer_jogada(self, linha:int, coluna:int, peca:str): #Coloca a peça na posição escolhida
        self.tabuleiro[linha][coluna] = peca

    def verificar_vitoria(self, linha:int, coluna:int, peca:str) -> bool: #Verifica se a jogada realizada resultou na vitória do jogador que a realizou
        if (self._checar_horizontal(linha, peca) or 
            self._checar_vertical(coluna, peca) or
            self._checar_diagonal_principal(linha, coluna, peca) or
            self._checar_diagonal_secundaria(linha, coluna, peca)):
            
            return True
        
        return False
    
    def _checar_horizontal(self,linha:int,peca:str) -> bool: #Checa se houve 4 peças na horizontal
        contador = 0
        for c in range(self.NUM_COLUNAS):
            if self.tabuleiro[linha][c] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
        return False
    
    def _checar_vertical(self,coluna:int,peca:str) -> bool: #Checa se houve 4 peças na vertical
        contador = 0
        for c in range(self.NUM_LINHAS):
            if self.tabuleiro[c][coluna] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
        return False
    
    def _checar_diagonal_principal(self,linha:int,coluna:int,peca:str) -> bool: #Testa se houve 4 peças na diagonal principal
        temp_lin, temp_col = linha, coluna
        
        while temp_lin > 0 and temp_col > 0:
            temp_lin -= 1
            temp_col -= 1
        
      
        contador = 0

        while temp_lin < self.NUM_LINHAS and temp_col < self.NUM_COLUNAS:
            
            if self.tabuleiro[temp_lin][temp_col] == peca:
                contador += 1
                if contador >= 4:
                    return True
            else:
                contador = 0
            
           
            temp_lin += 1
            temp_col += 1
            
        return False
    
    def _checar_diagonal_secundaria(self,linha:int,coluna:int,peca:str) -> bool: #Testa se houve 4 peças na diagonal secundária
        temp_lin , temp_col = linha, coluna
        while temp_lin > 0 and temp_col < self.NUM_COLUNAS - 1:
            temp_lin -= 1
            temp_col += 1
        
        contador = 0

        while temp_lin < self.NUM_LINHAS - 1 and temp_col > 0:
        
            if self.tabuleiro[temp_lin][temp_col] == peca:
                contador +=1 
                if contador >=4:
                    return True
            else:
                contador = 0

            temp_lin += 1
            temp_col -= 1
        
        return False
    



        


        
