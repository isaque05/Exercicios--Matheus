
print('bom dia tudo bem com vc hoje')
# Inicializando a fila de atendimento como uma lista vazia
fila_de_atendimento = []

# Adicionar clientes à fila
fila_de_atendimento.append("João")
print(f"Cliente João foi adicionado à fila.")
fila_de_atendimento.append("Maria")
print(f"Cliente Maria foi adicionado à fila.")
fila_de_atendimento.append("José")
print(f"Cliente José foi adicionado à fila.")

# Mostrar a fila de atendimento
if fila_de_atendimento:
    print("Fila de atendimento:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")

# Atender o próximo cliente da fila
if fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"Cliente {cliente} foi atendido.")
else:
    print("Não há clientes para atender.")

# Mostrar a fila de atendimento após atendimento
if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")

# Atender o próximo cliente da fila
if fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"\nCliente {cliente} foi atendido.")
else:
    print("\nNão há clientes para atender.")

# Mostrar a fila de atendimento após atendimento
if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")

# Atender todos os clientes restantes da fila
while fila_de_atendimento:
    cliente = fila_de_atendimento.pop(0)
    print(f"\nCliente {cliente} foi atendido.")

#  após atendimento de todos os clientes
if fila_de_atendimento:
    print("\nFila de atendimento atualizada:")
    for i, cliente in enumerate(fila_de_atendimento, start=1):
        print(f"{i}. {cliente}")
else:
    print("Fila de atendimento está vazia.")