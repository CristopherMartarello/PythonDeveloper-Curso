class Carro(): #definindo a classe Carro
    """Essa é a classe carro. Essa classe é utilizada para instanciar novos carros em nosso programa.""" #Docstring
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia): #definindo os ATRIBUTOS que a classe irá possuir
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0 #default
        self.is_ligado = False   #default
        self.velocidade = 0      #default

    def __del__(self): #método __del__ serve para quando os objetos não são mais utilizados e precisamos limpar memória.
        print("O objeto foi removido da memória.")

    def abastecer(self, qtd_combustivelInformada):
        """O método abastecer recebe como parametro a quantidade de combustivel e incrementa no atributo qtd_combustivel do objeto carro""" #Docstring
        self.qtd_combustivel += qtd_combustivelInformada

    def ligar(self):       #método ligar
        if(self.is_ligado == True):
            print(f"O carro já está ligado!")
        else:
            self.is_ligado = True
            print(f"O carro foi ligado.")

    def desligar(self):    #método desligar
        if(self.is_ligado == False):
            print(f"O carro já está desligado!")
        else:
            self.is_ligado = False

    def acelerar(self, velocidadeDesejada):
        if(self.is_ligado == True):
            self.velocidade += velocidadeDesejada
        else:
            print("O carro precisa estar ligado para ser acelerado.")

