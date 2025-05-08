import random
import string
import json
import os
# Escolinha
# Gerador do Ra dos alunos
def GeradorRA(tamanho=12):
    caracteres = string.digits
    return "".join(random.choices(caracteres, k=tamanho))


arquivo = "Cadastro.json"

# carregar os Cadastro existentes (se houver)
def carregarCadastro():
    if os.path.exists(arquivo):
        with open(arquivo, "r") as r:
            return json.load(r)
    return{}
# Salvar o Cadastro no arquivo
def salvarCadastro(cadastros):
    with open(arquivo, "w") as f:
        json.dump(cadastros, f, indent=4)


def cadastroResponsavel():
    nomeResponsavel = input("Informe o nome do Responsavel : ")

    sexualidadeResponsavel = input("Qual a sua sexualidade? | Masculino(M) | Feminino(F) | : ")
    if sexualidadeResponsavel == "M":
        sexualidade = "Masculino"
    elif sexualidadeResponsavel == "F":
        sexualidade = "Feminino"
    else:
        print("Responda apenas com M ou F ambos tem q ser maiusculos")

    idadeResponsavel = int(input("Sua idade? : "))
    
    if idadeResponsavel < 18:
        print(f"{nomeResponsavel} você não pode fazer o cadastro vc e menor de idade")
    else:
        numeroContato = input(f"{nomeResponsavel} qual o seu Número d contato? : (16) ")
        cpfResponsavel = input("Qual o seu CPF? : ")
        gmailResponsavel = input("Qual o seu Gmail? : ")
        senhaResponsavel = input("Qual vai se a senha d acesso? : ")
    
    UsuarioResponsavel = {
        "Nome": nomeResponsavel,
        "Sexualidade": sexualidade,
        "Idade": idadeResponsavel,
        "Contato": numeroContato,
        "CPF": cpfResponsavel,
        "Gmail": gmailResponsavel,
        "Senha": senhaResponsavel
    }

    cadastros = carregarCadastro()
    IdResponsavel = f"Responsavel_{len(cadastros) + 1}"
    cadastros[IdResponsavel] = UsuarioResponsavel
    salvarCadastro(cadastros)

    print(f"{IdResponsavel} Foi cadastrado com sucesso!")




def cadastroFilho():
    nomeFilho = input("Informe o nome de seu filho : ")

    sexualidadeFilho = input("Qual a sexualidade de seu filho? | Masculino(M) | Feminino(F) | : ")
    if sexualidadeFilho == "M":
        sexualidade = "Masculino"
    elif sexualidadeFilho == "F":
        sexualidade = "Feminino"
    else:
        print("Responda apenas com M ou F ambos tem q ser maiusculos")

    if sexualidade == "Masculino":
        pronome1 = "do"
        pronome2 = "O"
    elif sexualidade == "Feminino":
        pronome1 = "da"
        pronome2 = "A"


    idadeFilho = int(input(f"Qual a idade {pronome1} {nomeFilho}? : "))
    pcdFilho = input(f"{pronome2} {nomeFilho} e PCD? | SIM | NÃO | :")
    
    if pcdFilho == "SIM":
        pcdFilho = True
    elif pcdFilho == "NÃO":
        pcdFilho == False
    else:
        print("Coloca em Maiusculo")
    
    cpfFilho = input(f"Qual o CPF {pronome1} {nomeFilho}? : ")
    print(f"O RA de seu filho é {GeradorRA()} ! Não Perca esse RA !")
    RaAluno = GeradorRA()

    UsuarioFilho = {
        "Nome": nomeFilho,
        "Sexualidade": sexualidade,
        "Idade": idadeFilho,
        "CPF": cpfFilho,
        "PCD": pcdFilho,
        "RA": RaAluno
    }

    cadastros = carregarCadastro()
    IdAluno = f"Aluno_{len(cadastros) + 1}"
    cadastros[IdAluno] = UsuarioFilho
    salvarCadastro(cadastros)


def loginResponsavel():
    nomeUsuario = input("Qual o nome do Usuario? : ")
    gmail = input("Qual o seu Gmail? : ")
    senha = input("Qual a sua senha? : ")

def loginAluno():
    RA = input("Informe seu RA : ")
    senhaRA= input("Senha do RA : ")
