
print('bom dia tudo bem com vc hoje')

# Lista de palavras
palavras = ['python', 'java', 'c++', 'ruby', 'javascript', 'html', 'css', 'php']

# Solicita ao usuário uma letra
letra = input("Digite uma letra para filtrar as palavras: ")

# Percorre a lista de palavras e imprime as que começam com a letra fornecida
print(f"Palavras que começam com '{letra}':")
for palavra in palavras:
    if palavra.startswith(letra):
        print(palavra)