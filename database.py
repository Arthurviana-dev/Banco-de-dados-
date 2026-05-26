from sqlalchemy import create_engine, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#  Configuração do Banco de dados
db = create_engine("sqlite:///meubanco.db")
Base = declarative_base()

#  criação das Tabelas com as informações do usuario e do livro
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    gmail = Column(String)
    senha = Column(String)
    ativo = Column(Boolean, default=True) # Corrigido: adicionado Column

    def __init__(self, nome, gmail, senha, ativo=True):
        self.nome = nome
        self.gmail = gmail
        self.senha = senha
        self.ativo = ativo

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, autoincrement=True) # Adicionado PK
    titulo = Column(String)
    qtd_paginas = Column(Integer)
    dono = Column(Integer, ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtd_paginas, dono):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono

# Criação das tabelas no arquivo .db
Base.metadata.create_all(bind=db)

# Sessão para manipulação de dados
Session = sessionmaker(bind=db)
session = Session()

# Criar,ler,atualizar dados do usuario ou livro (CRUD)

# Criar Usuário
novo_usuario = Usuario(nome="Arthur", gmail="qualquercoisa@gmail.com", senha="123")
session.add(novo_usuario)
session.commit()

# Buscar Usuário por gmail
usuario_arthur = session.query(Usuario).filter_by(gmail="qualquercoisa@gmail.com").first()

if usuario_arthur:
    # Editar Usuário
    usuario_arthur.nome = "Arthur Viana"
    
    # Criar Livro vinculado ao usuário
    novo_livro = Livro(titulo="Livro Irado", qtd_paginas=1000, dono=usuario_arthur.id)
    
    session.add(novo_livro)
    session.commit()

# Chamar todos os dados da tabela
lista_usuarios = session.query(Usuario).all()
for lista in lista_usuarios:
    print(f"Usuário: {lista.nome} | E-mail: {lista.gmail}")
