"""
Wellington Pereia Luiz  - pt-br - utf-8 - 25-04-2024
21_05.py
"""
# Exemplo 1: Singleton Clássico com __new__ (entender o padrão)
'''

class Singleton:
    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'\nCriando nova instancia: {cls.instance}')
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print('\n', s1 is s2, '\n')

'''

# Exemplo 2: Singleton aplicado ao banco de dados com SQLite
'''

import sqlite3
import os

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):

    def __init__(self):
        pasta_base = os.path.dirname(os.path.abspath(__file__))

        caminho_db = os.path.join(pasta_base, 'db.ifro')

        self.conn = sqlite3.connect(caminho_db)
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        return self.cursor

db1 = Database()
db2 = Database()

print('\n', db1 is db2, '\n')
        
'''

# Exemplo 3: Singleton com função decoradora
'''

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

log1 = Logger()
log2 = Logger()

print('\n', log1 is log2, '\n')

'''

# Exercício 1:
'''
class SistemaConfiguracao:
    def __new__(cls):
        if not hasattr(cls, 'instancia_unica'):
            cls.instancia_unica = super(SistemaConfiguracao, cls).__new__(cls)
            print(f'\nNova instância criada: {cls.instancia_unica}')
            cls.instancia_unica.debug_ativo = False
            cls.instancia_unica.versao_sistema = '1.0.0'
        return cls.instancia_unica

config1 = SistemaConfiguracao()
config2 = SistemaConfiguracao()

config1.versao_sistema = '1.0.1'
config2.debug_ativo = True

print('\nVersão (instância 1):', config1.versao_sistema)
print('Versão (instância 2):', config2.versao_sistema)

print('\nDebug (instância 1):', config1.debug_ativo)
print('Debug (instância 2):', config2.debug_ativo)

'''

# Exercício 2:
'''
import os
import sqlite3

class MetaInstanciaUnica(type):
    _objetos = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._objetos:
            cls._objetos[cls] = super(MetaInstanciaUnica, cls).__call__(*args, **kwargs)
        return cls._objetos[cls]

class ConexaoBanco(metaclass=MetaInstanciaUnica):

    def __init__(self):
        diretorio_base = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(diretorio_base, 'clientes.db')

        self.conexao = sqlite3.connect(caminho_arquivo)
        self.cursor = self.conexao.cursor()
        self._criar_tabela()

    def _criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        self.conexao.commit()

    def adicionar_cliente(self, nome, email):
        self.cursor.execute('INSERT INTO cliente (nome, email) VALUES (?, ?)', (nome, email))
        self.conexao.commit()

    def obter_clientes(self):
        self.cursor.execute('SELECT * FROM cliente')
        return self.cursor.fetchall()
    
    def encerrar_conexao(self):
        self.conexao.close()

banco = ConexaoBanco()

banco.adicionar_cliente('João da Silva', 'joao.silva@gmail.com')
banco.adicionar_cliente('Maria Oliveira', 'maria.oliveira@gmail.com')

print('\nClientes cadastrados:')
for cliente in banco.obter_clientes():
    print(cliente)

banco.encerrar_conexao()

'''

# Exercício 3:
'''
class MetaInstanciaLog(type):
    _unicos = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._unicos:
            cls._unicos[cls] = super().__call__(*args, **kwargs)
        return cls._unicos[cls]

class RegistroLog(metaclass=MetaInstanciaLog):
    historico = []

    def salvar_log(self, texto):
        self.historico.append(texto)

    def mostrar_logs(self):
        for entrada in self.historico:
            print(entrada)

logger1 = RegistroLog()
logger2 = RegistroLog()

logger1.salvar_log('Log criado por logger1')
logger2.salvar_log('Log criado por logger2')

logger1.mostrar_logs()

'''

# Criando  um script básico do flask (app.py) 
 
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Olá Mundo!!! Bem-vindo ao sistema flask</h1> <a href="/sobre">Sobre</a>'

@app.route('/sobre')
def sobre():
    return '<p>Este é um sistema de exemplo para a introdução ao Flask</p> <a href="/">Home</a>'

if __name__ == '__main__':
    app.run(debug=True)


'''