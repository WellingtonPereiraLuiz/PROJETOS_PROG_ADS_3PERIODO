class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
     contador = 6999

     def __init__(self, liminte, saldo):
         self.__numero = ContaCorrente.contador + 1
         self.__limite = liminte
         self.__saldo = saldo
         ContaCorrente.contador = self.__numero
    