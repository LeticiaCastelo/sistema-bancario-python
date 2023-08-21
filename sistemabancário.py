from time import sleep  # Para finalizar o programa

print(16*'\033[36m=-') 
print('{:^30}'.format('CLASSIC BANK'))
print(16*'=-')    
print("\033[1mWelcome to Classic Bank!") # Cordialidade para ficar bonito

saldo = 0
limite = 500   # Declaração de variáveis
extrato = " "
numerosaques = 0
LIMITE_SAQUES = 3

menu = '''\033[0m
[D] Depositar   
[S] Sacar
[E] Extrato
[Q] Sair ''' # Menu de opções disponíveis

print(menu)
while True:
    opção = (str(input("\033[0m=> Selencione uma opção: "))).strip() .upper() #strip para remover espaços inúteis 
    if opção == "D":                                                           #upper para a resposta dada a opção ficar em maiúsculo
        valor = float(int(input("Informe o valor do depósito: R$ ")))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\033[1;31mA operação falhou! O valor informado é inválido!")

    elif opção == "S":
        valor = float(input("\033[1minforme o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numerosaques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("\033[1;31mA operação falhou! Você não tem saldo suficente.") # red color 

        elif excedeu_limite:
            print("\033[1;31mOperação falhou! O valor do saque excede o limite.") # red color 

        elif excedeu_saques:
            print("\033[1;31mOperação falhou! Número máximo de saques excedido.") # red color 

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" 
            numerosaques += 1
         
        else:
            print("\033[1;31mOperação falhou! O valor informado é inválido!")
    
    elif opção == "E":
        print("\033[0m============ EXTRATO ============")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("====================================")
    
    elif opção == 'Q':
        print('\033[1;31mFinalizando operação bancária...') 
        sleep(1.5) # from time import sleep
        break 
    
else:
 print("\033[1;31mOpcão inválida! Por favor selecione novamente uma opção válida.")