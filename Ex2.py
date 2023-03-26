n = int(input('Digite um número: '))

n1, n2 = 0, 1

while n1 < n:
    n1, n2 = n2, n1 + n2
if n1 == n:
    print('Este número pertence a sequência de Fibonacci')
else:
    print('Este número não pertence a sequência de Fibonacci')

