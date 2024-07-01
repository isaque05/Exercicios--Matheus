#atividade(r9)
print('bom dia tudo bem com vc hoje')

print("Calculadora Simples")
print("Operações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Solicita ao usuário que escolha uma operação
opcao = int(input("Escolha uma operação (1/2/3/4): "))

# Solicita ao usuário que entre com os números para a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executa a operação selecionada com base na opção escolhida
if opcao == 1:
    resultado = num1 + num2
    operacao = "+"
elif opcao == 2:
    resultado = num1 - num2
    operacao = "-"
elif opcao == 3:
    resultado = num1 * num2
    operacao = "*"
elif opcao == 4:
    # Verifica se o divisor é zero para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        operacao = "/"
    else:
        resultado = "Erro: divisão por zero"
        operacao = "/"
else:
    print("Opção inválida. Por favor, escolha uma operação válida.")
    exit()

# Imprime o resultado da operação
print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")