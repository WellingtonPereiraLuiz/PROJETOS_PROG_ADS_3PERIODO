
class Lampada:
    def __init__(self, volts, cor, tecnologia, luminosiadade, status):
        self.volts = volts
        self.cor  = cor
        self.tecnologia = tecnologia
        self.luminosidade = luminosiadade
        self.status = status   #Atributo publico
        #self.__status = "ligada"    atributo privado

    def ligar(self):
        self.status = "Desligado"
        return print('Lampada ', self.status)
    
    def desligar(self):
        self.status = "Ligado"
        return print('Lampada ', self.status)

lampada_sl = Lampada(110, "branca", "led", 40, "desligado")
lampada_sl.ligar()

lampada_qt = Lampada(220, "vermelha", "florescente", 80, "desligado")
lampada_qt.ligar()

lampada_cz = Lampada("bivolt", "amarela", "filamento", 60, "ligado")
lampada_cz.desligar()

print("\nLampada Sala!")
print("Volts: ", lampada_sl.volts)
print("Cor: ", lampada_sl.cor)
print("Tecnologia: ", lampada_sl.tecnologia)
print("Luminosidade: ", lampada_sl.luminosidade)
print("Status: ", lampada_sl.status)

print("\nLampada Quarto!")
print("Volts: ", lampada_qt.volts)
print("Cor: ", lampada_qt.cor)
print("Tecnologia: ", lampada_qt.tecnologia)
print("Luminosidade: ", lampada_qt.luminosidade)
print("Status: ", lampada_qt.status)

print("\nLampada Cozinha!")
print("Volts: ", lampada_cz.volts)
print("Cor: ", lampada_cz.cor)
print("Tecnologia: ", lampada_cz.tecnologia)
print("Luminosidade: ", lampada_cz.luminosidade)
print("Status: ", lampada_cz.status)
