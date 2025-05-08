# Escolinha

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


def cadastroFilho():
    nomeFilho = input("Informe o nome de seu filho : ")

    sexualidadeFilho = input(f"Qual a sexualidade de seu filho? : ")
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
    cpfFilho = input(f"Qual o CPF {pronome1} {nomeFilho}? : ")


def loginResponsavel():
    nomeUsuario = input("Qual o nome do Usuario? : ")
    gmail = input("Qual o seu Gmail? : ")
    senha = input("Qual a sua senha? : ")

def loginAluno():
    RA = input("Informe seu RA : ")
    senhaRA= input("Senha do RA : ")
