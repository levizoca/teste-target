import json

with open('dados.json') as file:
    dados = json.load(file)

# O menor valor de faturamento ocorrido em um dia do mês;
def menorvalor(dados):
    menor_valor = min(dados, key=lambda d : d['valor'])['valor']
    return [ item for item in dados if item['valor'] == menor_valor]

print('O(s) menor(res) de faturamento do mês: ',menorvalor(dados))

# O maior valor de faturamento ocorrido em um dia do mês;
def maiorvalor(dados):
    maior_valor = max(dados, key=lambda d : d['valor'])['valor']
    return [ item for item in dados if item['valor'] == maior_valor]

print('O(s) maior(res) de faturamento do mês: ', maiorvalor(dados))

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal;
def media(dados):
    media = sum(dado['valor'] for dado in dados) / len(dados)
    return [ item for item in dados if item['valor'] > media]

print('A média mensal de faturamento: ', sum(dado['valor'] for dado in dados) / len(dados))
print('O número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ', len(media(dados)))