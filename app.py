import os

print('Sabor Express\n')

print('1. Cadastrar Restaurante')
print('2. Listar Restaurante')
print('3. Ativar Restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurante')
elif opcao_escolhida == 3:
    print('Ativar Restaurante')
else:
    finalizar_app()