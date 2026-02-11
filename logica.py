#Lógica do caça-palavras
import random

tam_matriz = 20              

class Tabuleiro: #Classe criadora do tabuleiro
    #Construtor
    def __init__(self, tam_matriz):
        self.tam_matriz = tam_matriz

    def criar_matriz_vazia(self): 
        matriz =[]

        for i in range(self.tam_matriz):
            linha = []
            for j in range(self.tam_matriz):
                linha.append(" ") #adiciona espaço vazio em cada coluna
            matriz.append(linha) #adiciona uma linha completa na matriz

        return matriz


class AdicionarPalavras:
    #Construtor, definição de variáveis 
    def __init__(self, matriz, palavra):
        self.matriz = matriz
        self.palavra = palavra.upper()
        self.tam_palavra = len(self.palavra)
        self.tam_matriz = len(self.matriz)

    def adicionar_palavra(self):

        for tentativa in range(50): #Sorteia 50 vezes a posição 
            direcao = random.choice(['Horizontal', 'Vertical'])

            if direcao == 'Horizontal': #Gera o tamanho das letras e as coloca de acordo com o número de seu tamanho
                linha = random.randint(0, self.tam_matriz - 1)
                coluna = random.randint(0, self.tam_matriz - self.tam_palavra)
            else:
                linha = random.randint(0, self.tam_matriz - self.tam_palavra)
                coluna = random.randint(0, self.tam_matriz - 1)

        #Verifica o espaço livre da palavra para adiciona-lá
            posicao_livre = True
            for i in range(self.tam_palavra):
                if direcao == 'Horizontal':
                    letra_atual = self.matriz[linha][coluna + i]
                else:
                    letra_atual = self.matriz[linha + i][coluna]

#Caso os espaço estão preenchidos e as letras são diferentes das que se deseja adicionar
                if letra_atual != " " and letra_atual != self.palavra[i]:
                    posicao_livre = False
                    break #Encerra a verificação pois sabe que não a como adicionar

            if posicao_livre:
                for i in range(self.tam_palavra):
                    if direcao == 'Horizontal':
                        self.matriz[linha][coluna + i] = self.palavra[i]
                    else:
                        self.matriz[linha + i][coluna] = self.palavra[i]
                return True #palavra adicionada com sucesso
        return False #Palavra não adicionada

class FecharEspacos:
    @staticmethod
    def preencher_espacos(matriz):
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] == " ":
                    matriz[linha][coluna] = random.choice(alfabeto)
    
        return matriz


class BuscarPalavras:

    def __init__(self, arquivo):

        self.arquivo = arquivo
        self.palavras = []

    def carregar_palavras_tema(self, tema_escolhido):
        self.lista_palavras = []
        lendo = False

        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip() 
                if not linha:
                    continue


                if linha.upper() == f"[{tema_escolhido.upper()}]":
                    lendo = True
                    continue

                if linha.startswith("[") and lendo:
                    break

                if lendo and linha:
                    self.lista_palavras.append(linha.upper())


        return self.lista_palavras        


class GerarCacaPalavras: 
    #Construtor
    def __init__(self, tam_matriz):
        self.tam_matriz = tam_matriz
    
    def gerar_caca_palavras(self, lista_palavras):
        tabuleiro = Tabuleiro(self.tam_matriz).criar_matriz_vazia()

        #adiciona palavras da lista
        for palavra in lista_palavras:
            adicionador = AdicionarPalavras(tabuleiro, palavra)
            conseguiu = adicionador.adicionar_palavra()

            if conseguiu:
                print(f"Palavra '{palavra}' Colocada com sucesso!")
            else:
                print(f"Não foi possível adicionar a palavra{palavra}")

        tabuleiro_final = FecharEspacos.preencher_espacos(tabuleiro)

        return tabuleiro_final    
