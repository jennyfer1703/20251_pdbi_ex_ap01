import calculadora
def menu():
    while True:
        print("Escolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")
        
        opcao = input("Digite sua opção: ")
        
        
        if opcao == '0':
            print("\nSaindo...")
            break
        
        if opcao in ['1', '2', '3', '4']:
            a = float(input("\nDigite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                print(f"\nResultado: {a} + {b} = {calculadora.somar(a, b)}\n")
            elif opcao == '2':
                print(f"\nResultado: {a} - {b} = {calculadora.subtrair(a, b)}\n")
            elif opcao == '3':
                print(f"\nResultado: {a} * {b} = {calculadora.multiplicar(a, b)}\n")
            elif opcao == '4':
                print(f"\nResultado: {a} / {b} = {calculadora.dividir(a, b)}\n")
        else:
            print("\nOpção inválida! Tente novamente.")

menu()