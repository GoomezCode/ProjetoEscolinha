from datetime import datetime
from baseCadastro import cadastroResponsavel, cadastroFilho, loginAluno, loginResponsavel

horaAtual = datetime.now().hour

if horaAtual <=5:
    saudacao = "Boa Madrugada!"
elif horaAtual <= 12:
    saudacao = "Bom dia!"
elif horaAtual <=18:
    saudacao = "Boa tarde!"
elif horaAtual <=23:
    saudacao = "Boa noite!"


print(f"{saudacao}, Bem vindo(a) ao APP da Escola Isaac")
print("")
pergunta1 = input("Você é | Aluno | Responsavel | ? : ")

if pergunta1 == "Aluno":
        print("Olá Aluno Faça seu cadastro : ")
        print("")

        print(loginAluno())
elif pergunta1 == "Responsavel":
        
    pergunta2 = input("Você quer fazer | Login | Registro | ? : ")
    print("")

    if pergunta2 == "login":    
            print("Olá Pais faça o seu Login logo abaixo : ")
            print("")
            print(loginResponsavel())
    elif pergunta2 == "Registro":
            print(cadastroResponsavel())
            print("")
            pergunta3 = input("Você dejesa fazer o Registro de seu filho em nossa Escola? | SIM | NÃO | : ")

    if pergunta3 == "SIM":
            print("Cadastro de seu filho na Escola Issac")
            print()
            print(cadastroFilho())
    elif pergunta3 == "NÃO":
            print("Cadastro bem sucedido")
            print()
            print("Não perca tempo, Cadastre seu filho na melhor escola da Cidade")
    else:
            print("Responda Cerinho como tá escrito para n dar erro")
