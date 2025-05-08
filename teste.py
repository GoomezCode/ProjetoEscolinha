import json
import os

arquivo = "Cadastro.json"

# carrgar os Cadastros existentes (se houver)
def carregarCadastro():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as r:
            return json.load(r)
    return{}

# Salva os cadastros no arquivo
def salvarCadastro(cadastros):
    with open(arquivo, 'w') as f:
        json.dump(cadastros, f, indent=4)


def cadastrarUsuario():

    nome = input("Nome: ")
    gmail = input("Gmail: ")
    idade = input("Idade: ")

    usuario = {
        "Nome": nome,
        "Gmail": gmail,
        "Idade": idade
    }

    cadastros = carregarCadastro()
    proximoId = f"aluno{len(cadastros) + 1}"
    cadastros[proximoId] = usuario
    salvarCadastro(cadastros)

    print(f"{proximoId} foi cadastrado com sucesso! ")

cadastrarUsuario()
