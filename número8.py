#atividae(r8)
print('bom dia tudo bem com vc hoje')

# Inicializa a variável para armazenar a soma
soma = 0

# Loop para pedir 10 números
for i in range(10):
    # Pedir um número ao usuário
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # Adicionar o número à soma total
    soma += numero

# Imprimir a soma total dos números
print(f"A soma dos 10 números é: {soma}")