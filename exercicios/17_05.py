"""EXEMPLO 1
from abc import ABC, abstractmethod

class Veiculo(ABC):  # Classe abstrata
    @abstractmethod
    def mover(self):
        pass


# Subclasse concreta
class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo sobre quatro rodas.")


# Outra subclasse concreta
class Moto(Veiculo):
    def mover(self):
        print("A moto está se movendo sobre duas rodas.")


# Testando as classes
meu_carro = Carro()
minha_moto = Moto()

meu_carro.mover()
minha_moto.mover()
"""

"""EXERCÍCIO 1

from abc import ABC, abstractmethod

# Classe abstrata Funcionario
class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Subclasse Gerente
class Gerente(Funcionario):
    def calcular_salario(self):
        return 8000.00

# Subclasse Estagiario
class Estagiario(Funcionario):
    def calcular_salario(self):
        return 1500.00

# Criando objetos
gerente = Gerente()
estagiario = Estagiario()

# Imprimindo os salários
print(f"Salário do gerente: R$ {gerente.calcular_salario():.2f}")
print(f"Salário do estagiário: R$ {estagiario.calcular_salario():.2f}")
"""

"""EXERCÍCIO 2

from abc import ABC, abstractmethod

# Classe abstrata com atributo nome
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

# Subclasse Professor
class Professor(Funcionario):
    def calcular_salario(self):
        return 5000.00

# Subclasse Tecnico
class Tecnico(Funcionario):
    def calcular_salario(self):
        return 3000.00

# Criando objetos
professor = Professor("Carlos")
tecnico = Tecnico("Ana")

# Imprimindo nome e salário
print(f"{professor.nome} - Salário: R$ {professor.calcular_salario():.2f}")
print(f"{tecnico.nome} - Salário: R$ {tecnico.calcular_salario():.2f}")
"""

"""EXERCÍCIO 3


from abc import ABC, abstractmethod

# Classe abstrata
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

# Subclasse CLT
class CLT(Funcionario):
    def calcular_salario(self):
        return 4000.00

# Subclasse Temporario
class Temporario(Funcionario):
    def calcular_salario(self):
        return 2500.00

tipo = input("Informe o tipo de contrato (CLT ou Temporario): ").strip().lower()
nome = input("Informe o nome do funcionário: ").strip()


if tipo == "clt":
    funcionario = CLT(nome)
elif tipo == "temporario":
    funcionario = Temporario(nome)
else:
    print("Tipo de contrato inválido!")
    funcionario = None

if funcionario:
    print(f"{funcionario.nome} - Salário: R$ {funcionario.calcular_salario():.2f}")  
"""

"""EXERCÍCIO 4

from abc import ABC, abstractmethod

# Superclasse abstrata
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_salario(self):
        pass

# Subclasse Analista
class Analista(Funcionario):
    def calcular_salario(self):
        return 6000.00

# Subclasse Auxiliar
class Auxiliar(Funcionario):
    def calcular_salario(self):
        return 2000.00

# Subclasse Gerente
class Gerente(Funcionario):
    def calcular_salario(self):
        return 8000.00

# Lista de funcionários
funcionarios = [
    Analista("João"),
    Auxiliar("Beatriz"),
    Gerente("Carlos"),
    Analista("Renata"),
    Auxiliar("Pedro")
]

# Usando polimorfismo para exibir todos os salários
for funcionario in funcionarios:
    print(f"{funcionario.nome} - Salário: R$ {funcionario.calcular_salario():.2f}")
"""