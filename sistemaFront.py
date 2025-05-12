from SistemaDados import funcionario, responsavei, aluno, admin, chamaSession

session = chamaSession()

fun = funcionario
pais = responsavei
Aluno = aluno
admin = admin

# adicionar Cadastro Funcionario
def cadastroFuncionario():

    print("---------------CADASTRO FUNCIONARIO---------------")
    print()

    Nome = input("Qual o seu Nome? : ")
    Idade = int(input("Qual a sua Idade? : "))
    Gmail = input("Qual o seu Gmail? : ")
    while True:
        Funcao = int(input("Qual a sua Função? | Estágiario(1) | Limpeza(2) | Professora(3) | Diretor(4) | Cordenador(5) | Recepção(6) | : "))
        if Funcao == 1:
            Funcao = "Estágiario"
            break
        elif Funcao == 2:
            Funcao = "Limpeza"
            break
        elif Funcao == 3:
            Funcao = "Professora"
            break
        elif Funcao == 4:
            Funcao = "Diretor"
            break
        elif Funcao == 5:
            Funcao = "Cordenador"
            break
        elif Funcao == 6:
            Funcao = "Recepção"
            break
        else:
            print("Não temos essa opção")
    Horario = int(input("Qual o seu Horario | Integral(1) | meioPeriodo(2) | : "))
    if Horario == 1:
        Horario = "Integral"
    elif Horario == 2:
        Horario = "meioPeriodo"
        Turno = int(input("Qual seu Turno? | Manhã(1) | Tarde(2) | noite(3) |  : "))
        while True:
            if Turno == 1:
                Turno = "Manhã"
                break
            elif Turno == 2:
                Turno = "Tarde"
                break
            elif Turno == 3:
                Turno = "Noite"
                break
            else:
                print("Preciso que coloque apenas as opções Disponiveis")
    else:
        print("Não n Temos essa opção")

    Salario = None
    Falta = None

    #Criando e postando o Cadastro no Banco de Dados
    funcionario = fun(nome=Nome, idade=Idade, gmail=Gmail, funcao=Funcao, horario=Horario, turno=Turno)
    session.add(funcionario)
    session.commit()
    print()
    print("---------------CADASTRO FEITO---------------")    
    
    return Funcao
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adicionar cadastro dos Responsavei para depois Fazer o cadastro dos Alunos
def cadastroResteAluno():
    print()
    print("---------------CADASTRO RESPONSAVEIS---------------")
    print()

    NomeP = input("Qual o seu Nome? : ")
    IdadeP = int(input("Qual a sua Idade? : "))
    RgP = int(input("Informe o seu RG : "))
    CpfP = int(input("Informe o seu CPF : "))
    GmailP = input("Qual o seu gmail? : ")
    NumTelP = int(input("Informe o numero de Contato : (16) "))
    ResidenciaP = input("Qual sua residencia? : ")


    while True:
        print()
        print("Vocẽ tem que fazer o cadastro de seu filho agr !!")
        Resposta = int(input("Tudo bem para Você? | Sim(1) | Não(2) | "))

        if Resposta == 1:
            print()
            print("---------------CADASTRO ALUNO---------------")
            print()

            NomeA = input("Qual o Nome do aluno? : ")
            IdadeA = int(input("Qual a Idade do Aluno? : "))
            TurmaA = input("Qual a Serie do Aluno? : ")

            while True:
                PcdA = int(input("O aluno e PCD(Pessoa com Deficiência) | Sim(1) | Não(2) | : "))

                if PcdA == 1:
                    PcdA = True
                    break
                elif PcdA == 2:
                    PcdA = False
                    break
                else:
                    print("Não temos essa opção somente as | 1 = Sim | 2 = Não | ")

            while True:
                RestAlimentarA = int(input("Seu Filho tem Restrição Alimentar? | Sim(1) | Não(2) | : "))

                if RestAlimentarA == 1:
                    RestAlimentarA = input("Quais Restrições? : ")
                    break
                elif RestAlimentarA == 2:
                    RestAlimentarA = "Não"
                    break
                else:
                    print("Não temos essa opção somente as | 1 = Sim | 2 = Não | ")

            while True:
                AlergiaA = int(input("Seu Filho tem alguma Alergia ? | Sim(1) | Não(2) | : "))
                
                if AlergiaA == 1:
                    AlergiaA = input("Quais Alergias? : ")
                    break
                elif AlergiaA == 2:
                    AlergiaA = "Não"
                    break
                else:
                    print("Não temos essa opção somente as | 1 = Sim | 2 = Não | ")
            NomePaisA = input("Informe o Nome do Responsavel : ")
            
            # Cadastro Responsaveis para Banco de Dados
            rest = pais(nome=NomeP, idade=IdadeP, rg=RgP, cpf=CpfP, gmail=GmailP, numTel=NumTelP, residencia=ResidenciaP)
            session.add(rest)
            session.commit()

            # Puxar o Gmail para identificar quem e o Responsavel
            restPessoa = session.query(responsavei).filter_by(gmail=rest.gmail).first()

            #Cadastro Alunos para Banco de Dados
            aluno = Aluno(nome=NomeA, idade=IdadeA, turma=TurmaA, pcd=PcdA, restAlimentar=RestAlimentarA, alergia=AlergiaA, nomePais=NomePaisA, responsavel=restPessoa.id)
            session.add(aluno)
            session.commit()
            break
        elif Resposta == 2:
            print("Então dps vc Volta e Refaz o seu cadastro e o cadastro de seu filho")
            break
        else:
            print("Não temos essa opção somente as | 1 = Sim | 2 = Não | ")
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print()
print("---------------CADASTRO Admin---------------")
print()

    # Tenho q Corrigir o admin - o Cadastro admin já vai ser criado Dependo do cargo q vc tiver No cadastroFuncionario

# # Deletar Cadastro do Banco de Dados
# delPessoa = session.query(fun).filter_by(id="").first()
# session.delete(delPessoa)
# session.commit()
