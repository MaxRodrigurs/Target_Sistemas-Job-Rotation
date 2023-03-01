num = int(input("Digite um número: "))

ant = 0
atual = 1

while atual <= num:
    if atual == num:
        print(f"O número {num} pertence à sequência de Fibonacci.")
        break
    next = ant + atual
    ant = atual
    atual = next
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")