
print('bom dia tudo bem com vc hoje')

# Solicita ao usuário para inserir um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é primo
if numero > 1:
    eh_primo = True  # Assume inicialmente que o número é primo
    # Verifica divisibilidade por números de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
else:
    eh_primo = False  # Números menores ou iguais a 1 não são primos

if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")