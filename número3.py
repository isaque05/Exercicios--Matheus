
print('bom dia tudo bem com vc hoje')
# Inicializando os primeiros números da sequência de Fibonacci
fib_sequence = []
a, b = 0, 1

# Gerando os primeiros 10 números da sequência
for _ in range(10):
    fib_sequence.append(a)
    a, b = b, a + b

# Exibindo os primeiros 10 números da sequência 
print("Os primeiros 10 números da sequência de Fibonacci são:")
print(fib_sequence)