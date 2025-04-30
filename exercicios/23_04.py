
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


# # 4 - A herança múltipla - implementação: 
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
#         return f'O {self._Animal__nome} nada.'
    
#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo em agua doce!'
    

# class Onitorrinco(Terrestre, Aquatico):
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo na terra e na agua doce!'
    
# # 5 - testando a classe multi derivada direta    
# perry = Onitorrinco('Perry')
# print("\n", perry.andar())
# print("\n", perry.nadar())
# print("\n", perry.cumprimentar())

# # 6 - Classe multi derivada indireta:
# class Pinguim(Onitorrinco):
#     def __init__(self, nome):
#         super().__init__(nome)

#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo na terra e na agua salgada!'
    
# # 7 - Testando classe multi derivada indireta 
# pinguim = Pinguim('Picolino')
# print()
# print(pinguim.nadar())
# print()
# print(pinguim.cumprimentar())

# #  8 - Analisando qual instância pertence o pinguim
# print()
# print(f'\nPinguim Picolino é da instancia pinguim?: {isinstance(pinguim, Pinguim)}')

# # 09 - ornitorrinco herda das classes Terrestre e Aquático: 
# class Ornitorrinco(Aquatico,Terrestre):
#     def __init__(self, nome):
#         super().__init__(nome)

#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo na terra e na agua doce'
    
# print()
# perry = Ornitorrinco('Perry')
# print(perry.cumprimentar())

# # 10 - Se não houver o método cumprimentar dentro da classe, aí entra o MRO
# class Ornitorrinco(Aquatico,Terrestre):
#     def __init__(self, nome):
#         super().__init__(nome)

# print()
# perry = Ornitorrinco('Perry')
# print(perry.cumprimentar())

# # 11 - Se a ordem da classe for alterada, o resultado será diferente: 
# class Ornitorrinco(Terrestre, Aquatico):
#     def __init__(self, nome):
#         super().__init__(nome)

# print()
# perry = Ornitorrinco('Perry')
# print(perry.cumprimentar())

# # 12 - Entendendo a ordem de execução de uma classe multi derivada
# class Ornitorrinco(Aquatico, Terrestre):
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def cumprimentar(self):
#         return f'Eu sou {self._Animal__nome} e vivo na terra e na agua doce'


# print()
# perry = Ornitorrinco('Perry')
# print(perry.cumprimentar())
# print(help(Ornitorrinco))


# # 13 - O overrinding é a melhor representação do polimorfismo
# class Animal(object): # Colocamos o objetc dentro da classe Animal, mas isso não é necessário, pois, por default toda classe em Python herda de objetc 
#     def __init__(self, nome):
#         self.__nome = nome

#     def emite_som(self):
#         raise NotADirectoryError('a classe filha precisa implementar esse metodo')
    
#     def come(self):
#         print(f'{self.__nome} esta comendo.')

# class Cachorro(Animal):
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def emite_som(self):
#         print(f'{self._Animal__nome} fala wau wau')

# class Gato(Animal):
#     def __init__(self, nome):
#         super().__init__(nome)
    
#     def emite_som(self):
#         print(f'{self._Animal__nome} fala miau miau')

# print()
# feliz = Gato("Feliz")
# feliz.come()
# feliz.emite_som()

# print()
# gerivaldo = Cachorro("Gerivaldo")
# gerivaldo.come()
# gerivaldo.emite_som()


# # 14 - Aplicando métodos mágicos 
# class Livros:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas

# # 15 - Testando
# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# print(f'\nLivro: {livro_1}')
# print(f'\nLivro: {livro_2}')

# # 16 - Tornando a informação representativa - __repr__(self):
# def __repr__(self):
#     return f'{self.__titulo} escrito por {self.__autor}'

# # 17 – Refatorando e testando a classe Livros com __repr__(self)
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __repr__(self):
#         return f'{self.__titulo} escrito por {self.__autor} - numero de paginas:{self.__paginas}'


# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# print(f'\nLivro: {livro_1}')
# print(f'\nLivro: {livro_2}')

# # 18 - Tornando a informação representativa para o usuário final - __str__(self)
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __str__(self):
#         return f'{self.__titulo} escrito por {self.__autor} - numero de paginas:{self.__paginas}'


# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# print(f'\nLivro: {livro_1}')
# print(f'\nLivro: {livro_2}')

# # 19 – Verificando o tamanho de um atributo usando - __len__(self)
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __len__(self):
#         return len(self.__titulo)
    

# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# print(f'\nTamanho do primeiro livro:', livro_1)
# print(f'\ntamanho do segundo Livro:', len(livro_2))


# # 20 – Apagando objetos da memória 
# del livro_1
# del livro_2


# # 21 – Apagando objetos da memória e retornando uma mensagem - __del__(self).
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __del__(self):
#         print(f'\nO objeto do tipo livro foi apagado da memoria.')
   

# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# del livro_1
# del livro_2

# # 22 - Concatenando objetos __add__(self, segundo_objeto)
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __str__(self):
#         return self.__titulo
    
#     def __add__(self, segunfo_objeto):
#         return f'Titulo livro_1: {self} - Titulo livro_2: {segunfo_objeto}'

# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)
# livro_2 = Livros('Programacao Funcional para Leigos', 'Jhon Paul Mueller',481)

# print(livro_1 + livro_2)


# # 23 - Multiplicando o valor do atributo de um objeto por um número
# class Livros:

#     def __init__(self, titulo, autor, paginas):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__paginas = paginas

#     def __str__(self):
#         return self.__titulo
    
#     def __mul__(self, numero):
#         if isinstance(numero, int):
#             mensagem = ''
#             for n in range(numero):
#                 mensagem += '-' + str(self)
#             return mensagem
#         return 'Não foi possivel multiplicar'
  

# livro_1 = Livros('Python: Guia Pratico do Basico ao Avancado','Rafael F. V. C. Santos', 225)

# print('\n', livro_1 * 3)
# print('\n', livro_1 * 'abc')

# # 24 - Importando o módulo e verificando as funções
# import datetime
# print()
# print(dir(datetime))

# 25 - Analisando o ano máximo e o ano mínimo para o datetime
import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# 26 - Retornando a data e horas corrente 
import datetime
print()
print(datetime.datetime.now())
print()
# 27 - Verificando a representação do método datetime -  year, month, day, hour, minute, second, microsecond 
print(repr(datetime.datetime.now()))

# 28 - Alterando os parâmetros de uma variável pelo datetime
import datetime

inicio = datetime.datetime.now()
print('Data e hora capturada pela variavel inicio:', inicio)

print()
inicio ==dd