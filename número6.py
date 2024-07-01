#atividade(r6)
print('bom dia tudo be com vc hoje')

# Inicializando as variáveis para encontrar o maior e o menor número
maior = None
menor = None

# Função para ler a lista de números fornecida pelo usuário
while True:
    try:
        # Pedir ao usuário para inserir números separados por espaço
        entrada = input("Digite os números separados por espaço: ")
        # Converte a entrada em uma lista de float
        lista_numeros = list(map(float, entrada.split()))
        
        if not lista_numeros:
            print("Lista vazia. Nenhum número fornecido.")
            continue
        
        # Inicializando maior e menor com o primeiro número da lista
        maior = lista_numeros[0]
        menor = lista_numeros[0]

        # Encontrando o maior e o menor número na lista
        for numero in lista_numeros:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        
        # Após encontrar, sair do loop de entrada
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite números separados por espaço.")

# Exibindo o resultado
if maior is not None and menor is not None:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")