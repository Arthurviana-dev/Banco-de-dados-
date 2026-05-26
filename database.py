from sqlalchemy import create_engine, Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

#criação das tabelas que armazenam as informações do usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    nome = Column("nome",String)
    gmail = Column("gmail",String)
    senha = Column("senha",String)
    ativo =  Column("ativo",Boolean)

    def __init__(self,nome,gmail,senha,ativo = True):
        self.nome = nome
        self.gmail = gmail
        self.senha = senha
        self.ativo = ativo

#criando o que cada livro armazena (objeto criado no banco de dados)
class Livro(Base):
    __tablename__ = "livros"
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    titulo = Column("Titulo",String)
    qtd_paginas = Column("paginas",Integer)
    dono = Column("dono",ForeignKey("usuarios.id"))

    def __init__(self,titulo,qtd_paginas,dono):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas
        self.dono = dono
        
Base.metadata.create_all(bind=db)
#criar uma consulta no banco de dados
lista_usuarios = session.query(Usuario).all()

#buscar um usuario por um gmail especifico sem precisar pegar todos
usuario_arthur = session.query(Usuario).filter_by(gmail ="qualquercoisa@gmail.com").first()
#criar,ler, atualizar e deletar dados do banco de dados (CRUD)
usuario = Usuario(nome = "arthur",gmail = "qualquercoisa@gmail.com",senha = "123123")
session.add(usuario)
session.commit()

#fazer uma edição no banco de dados exemplo: nome
usuario_arthur.nome = "arthur viana"
session.add(usuario_arthur)
session.commit()
#criando livro no banco de dados com cada informação armazenada na classe
livro = Livro(titulo = "Livro irado",qtd_paginas = 1000, dono = usuario_arthur.id)  
session.add(livro)
session.commit()

