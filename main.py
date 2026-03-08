print("""Operações:
Soma (1)
Subtração (2)
Divisão (3)
Multiplicação (4)
Potencia (5)
Medias /2 (6)
Sair (0)""")

opcao = input("Escolha sua operação:")

if opcao == "1":
    print("Você selecinou soma.")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("Digite seu segundo número: "))
    resultado = n1 + n2
    print("Resultado: ", resultado)

if opcao == "2":
    print("Você selecionou Subtração.")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("Digite seu segundo número: "))
    resultado = n1 - n2
    print("Resultado: ", resultado)
    
if opcao == "3":
    print("Você selecionou Divisão.")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("Digite seu segundo número: "))
    resultado = n1 / n2
    print("Resultado: ", resultado)

if opcao == "4":
    print("Você selecionou Multiplicação.")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("Digite seu segundo número: "))
    resultado = n1 * n2
    print("Resultado: ", resultado)

if opcao == "5":
    print("Você selecionou Potencias.")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("por quantas vezes você quer multiplicar esse número? "))
    resultado = n1 ** n2
    print("Resultado: ", resultado)
    
if opcao == "6":
    print("Você selecionou média de dois números")
    n1 = float(input("Digite seu primeiro número: "))
    n2 = float(input("Digite seu segundo número: "))
    resultado = (n1 + n2) /2
    print("Resultado: ", resultado)

if opcao == "0":
    print("Você selecionou sair.")
