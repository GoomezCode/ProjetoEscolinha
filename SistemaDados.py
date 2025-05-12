from sqlalchemy import create_engine,Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///BancoDadosEscolinha")

def chamaSession():
    Session = sessionmaker(bind=db)
    session = Session()
    return session
# Dentro desses dois vão ser criado as Tabelas de Dados 
Base = declarative_base()

class funcionario(Base):
    __tablename__= "funcionario"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    gmail = Column("Gmail", String)
    funcao = Column("Função", String)
    horario = Column("Horario", String)
    turno = Column("Turno", String)
    salario = Column("Salario", Integer)
    falta = Column("Falta", Integer)

    def ___init___(self, nome, idade, gmail, funcao, horario, turno, salario, falta):
        self.nome = nome
        self.idade = idade
        self.gmail = gmail
        self.funcao = funcao
        self.horario = horario
        self.turno = turno
        self.salario = salario
        self.falta = falta

class responsavei(Base):
    __tablename__="responsaveis"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    rg = Column("RG", Integer)
    cpf = Column("CPF", Integer)
    gmail = Column("Gmail", String) 
    numTel = Column("NumeroTelefone", Integer)
    residencia = Column("Residencia", String)

    def __init__(self, nome, idade, rg, cpf, gmail, numTel, residencia):
        
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.cpf = cpf
        self.gmail = gmail
        self.numTel = numTel
        self.residencia = residencia


class aluno(Base):
    __tablename__= "alunos"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nome =  Column("Nome", String)
    idade = Column("Idade", Integer)
    turma = Column("Turma", String)
    pcd = Column("AlunoPCD", Boolean)
    restAlimentar = Column("RestAlimentar", String)
    alergia = Column("Alergia", String)
    nomePais = Column("NomePais", String)
    responsavel = Column("Responsavel", String, ForeignKey(responsavei.id))

    def __init__(self, nome, idade, turma, pcd, restAlimentar, alergia, nomePais, responsavel):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.pcd = pcd
        self.restAlimentar = restAlimentar
        self.alergia = alergia
        self.nomePais = nomePais
        self.responsavel = responsavel
class admin(Base):
    __tablename__= "admin"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    funcao = Column("Função", String)
    horario = Column("Horario", String)
    gmail = Column("Gmail", String)
    senha = Column("Senha", String)

    def __init__(self, nome, idade, funcao, horario, gmail, senha):

        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.horario = horario
        self.gmail = gmail
        self.senha = senha
    
Base.metadata.create_all(bind=db)