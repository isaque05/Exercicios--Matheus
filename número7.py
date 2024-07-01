#atividade(r7)
print('bom dia tudo bem com vc hoje')

# Inicializando a lista vazia
lista_elementos = []

# Solicitando ao usuário para adicionar elementos à lista
while True:
    elemento = input("Digite um elemento para adicionar à lista (digite 'parar' para encerrar): ")
    
    if elemento.lower() == 'parar':
        break
    
    lista_elementos.append(elemento)

# Exibindo a lista completa
print("\nA lista completa é:")
print(lista_elementos)