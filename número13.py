
print('bom dia tudo bem com vc hoje')

soma = 0

while True:
    try:
        numero = int(input("Digite um número (ou 0 para sair): "))
        if numero == 0:
            break
        soma += numero
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print(f"A soma de todos os números digitados é: {soma}")