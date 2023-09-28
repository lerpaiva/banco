from classes import *
import getpass
import os







banco = Banco()
#Menu
def main():
    y = False
    
    trava = 0
    while y == False:
        
        try:
            menu = int(input("\n BEM-VINDO AO MMALT-PAY! \n \n [1] Conta \n [2] Cadastro \n [3] Sair \n \n Digite a opção desejada: "))
            match menu:
                case 1:
                    if trava == 0:
                        print("Nenhum usuário cadastrado.")
                        os.system("pause")
                        os.system("cls")

                    elif trava == 1: #teste
                        os.system("cls")
                        print("Preencha as informações para acessar sua conta. \n")
                        cpf = int(input("CPF: "))
                        senhaa = getpass.getpass("Digite sua senha: ")
                        cliente_encontrado = banco.validar_cliente_por_cpf_e_senha(cpf, senhaa)

                        if cliente_encontrado:
                            os.system("cls")
                            op = int(input(" \n [1] Saldo [2] Transferência \n [3] Depósito \n [4] Saque \n [5] Alterar dados \n [6] Excluir conta  \n [7] Voltar \n [8] Sair \n \n Digite a opção desejada: "))
                            match op:
                                case 1:
                                    os.system("cls")
                                    print("Este é seu saldo atual:")
                                    cliente_encontrado.getSaldo()
                                    os.system("pause")
                                case 2:
                                    os.system("cls")
                                    print("Para fazer uma transferencia, informe:")
                                    cpff = int(input(" CPF do destinatário: "))
                                    receptor = banco.validar_cliente_por_cpf_e_senha(cpff,"")
                                    if receptor:
                                        quantia = float(input("Quantia a transferir: "))
                                        cliente_encontrado.transferencia(quantia, receptor)
                                    else: 
                                        print("Alguma informação está incorreta")
                                    os.system("pause")
                                case 3:
                                    os.system("cls")
                                    print("Deposite aqui")
                                    print()
                                    val = float(input("Valor para o depósito: "))
                                    cliente_encontrado.depositar(val)
                                    os.system("pause")
                                case 4:
                                    os.system("cls")
                                    print("Saque aqui")
                                    print()
                                    saq = float (input("Valor a sacar: "))
                                    cliente_encontrado.sacar(saq)
                                    os.system("pause")
                                case 5:
                                    os.system("cls")
                                    menu2 = int(input("\n O que você deseja alterar? \n \n [1] Nome \n [2] Email \n [3] Telefone \n [4] CPF \n [5] Senha \n [6] Idade \n \n Digite a opção desejada: "))
                                    match menu2:
                                        case 1:
                                            novo_nome = input("Digite o novo nome: ")
                                            cliente_encontrado.setNome(novo_nome)
                                        case 2:
                                            novo_email = input("Digite o novo email: ")
                                            cliente_encontrado.setEmail(novo_email)
                                        case 3:
                                            novo_telefone = input("Digite o novo telefone: ")
                                            cliente_encontrado.setTelefone(novo_telefone)
                                        case 4:   
                                            novo_cpf = input("Digite o novo CPF: ")
                                            cliente_encontrado.setCPF(novo_cpf)
                                        case 5:
                                            nova_senha = input("Digite a nova senha: ")
                                            cliente_encontrado.setSenha(nova_senha)
                                        case 6:
                                            nova_idade = input("Digite a nova idade: ")
                                            cliente_encontrado.setIdade(nova_idade)
                                    os.system("pause")
                            
                                case 6:
                                    os.system("cls")
                                    print("Exclusão de conta")
                                    cpppf = int(input("Informe o cpf da conta a ser apagada"))
                                    banco.excluir_conta(cpppf)
                                    trava =0
                                    os.system("pause")
                                case 7:
                                    os.system("cls")
                                case 8:
                                    y = True
                                case _:
                                    os.system("cls")
                                    print("Opção inválida.")
                                    os.system("pause")
                        else:
                            os.system("cls")
                            print("Cliente não encontrado.")
                            os.system("pause")
                
                #Cadastro
                case 2:
                    try:
                        trava = 1
                        os.system("cls")
                        print("Preencha as informações abaixo \n")
                        nome = input("Nome: ")
                        cpf = int(input("CPF: "))
                        idade = int(input("Idade: "))
                        telefone = input("Telefone: ")
                        email = input("Email: ")
                        senha = getpass.getpass("Digite sua senha: ")
                        banco.adicionar_cliente(nome, cpf, idade, telefone, email, senha, saldo=0)

                        if idade < 18:
                            print("\nDesculpe, você não pode ter uma conta se for menor de 18 anos.")
                            
                        else:
                            print("\nUsuário cadastrado com sucesso!")
                        op = int(input("\n [1] Voltar \n [2] Sair \n \nDigite a opção desejada: ")) #Opções para voltar/sair do software.

                        if op == 1: #Voltar
                            y = False
        
                            os.system("cls")

                        elif op == 2: #Sair
                            y = True
                        

                        else: #Opção inválida
                            print("Opção inválida")
                        os.system("pause")
                            
                    except Exception in erro:
                       print("Opção inválida")
                    
                case 3:
                    y = True
                
                case _:
                    os.system("cls")
                    print("Opção inválida")
                    os.system("pause")

        except Exception as erro:
            print("\n Opção inválida. \n")
            os.system("pause")
            os.system("cls")

