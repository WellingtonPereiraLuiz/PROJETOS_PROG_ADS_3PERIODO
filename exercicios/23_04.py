
# #METODO super()
# # Segundo  F.V.C  (2020,  página  232):  “O  método super() faz a coleta dos atributos da super classe (classe pai)
# class Animal: 
#     def __init__(self, nome, especie):
#         self.__nome = nome
#         self.__especie = especie

#     def som(self, som):
#         print(f"O som que o {self.__nome} faz chama-se: {som}")

# class Elefante(Animal):
#     def __init__(self, nome, especie, raca):
#         super().__init__(nome, especie)
#         super().som("bramido")
#         self.__raca = raca

# class Girafa(Animal):
#     def __init__(self, nome, especie, raca):
#         super().__init__(nome, especie)
#         self.__raca = raca


# dumbo = Elefante('Elefante','Africano', 'Loxodonta Africana')
# gisela = Girafa('Girafa', 'Africana', 'Giraffidae')
# gisela.som("Zumbido")



# #HERANCA MULTIPLA
# # 1 - Por multiderivação direta:
# class SuperClasse_1:
#     pass
# class SuperClasse_2:
#     pass
# class SuperClasse_3:
#     pass

# class Multi_Derivada_Direta(SuperClasse_1,SuperClasse_2,SuperClasse_3):
#     pass


# #2 - Por multiderivação indireta: 
# class SuperClasse_1:
#     pass
# class SuperClasse_2(SuperClasse_1):
#     pass
# class SuperClasse_3(SuperClasse_2):
#     pass

# class Multi_Derivada_Direta(SuperClasse_3):
#     pass


# # 3 - A herança múltipla - implementação 
# class Animal:
#     def __init__(self, nome):
#         self.__nome = nome
        
#     def cumprimentar(self):
#         return f"Eu sou{self.__nome}"
                

# class Terrestre(Animal): 
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def andar(self):
#         return f'Ola eu sou {self._Animal__nome} e estou andando pela mata'
    
#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo em florestas tropicais!'
    
# class Aquatico(Animal): 
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def nadar(self):
#         return f'O {self._Animal__nome} nada e é um peixe filtrante.'
    
#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo em agua doce!'
    

# tatu = Terrestre('Tatu Bola')
# print()
# print(tatu.andar())
# print()
# print(tatu.cumprimentar())
# print(f'\nTatu Bola é instancia de Tatu?: {isinstance(tatu, Terrestre)}')


# peixe = Aquatico('tambaqui')
# print()
# print(peixe.nadar())
# print()
# print(peixe.cumprimentar())
# print(f'\nTambaqui é instancia de peixe?: {isinstance(peixe, Aquatico)}')


# 4 - A herança múltipla - implementação: 
class Animal:
    def __init__(self, nome):
        self.__nome = nome
        
    def cumprimentar(self):
        return f"Eu sou{self.__nome}"
                

class Terrestre(Animal): 
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'Ola eu sou {self._Animal__nome} e estou andando pela mata'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo em florestas tropicais!'
    


class Aquatico(Animal): 
    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'O {self._Animal__nome} nada.'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo em agua doce!'
    

class Onitorrinco(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo na terra e na agua doce!'
    
# 5 - testando a classe multi derivada direta    
perry = Onitorrinco('Perry')
print("\n", perry.andar())
print("\n", perry.nadar())
print("\n", perry.cumprimentar())

# 6 - Classe multi derivada indireta:
class Pinguim(Onitorrinco):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e vivo na terra e na agua salgada!'
    
# 7 - Testando classe multi derivada indireta 
pinguim = Pinguim('Picolino')
print()
print(pinguim.nadar())
print()
print(pinguim.cumprimentar())

#  8 - Analisando qual instância pertence o pinguim
print()
print(f'\nPinguim Picolino é da instancia pinguim?: {isinstance(pinguim, Pinguim)}')

