import json

with open("dados.json", "r") as f:
    dados = json.load(f)

menor_valor = min(dados)
maior_valor = max(dados)

dados_feriados = [f for f in dados if f > 0]  
med = sum(dados_feriados) / len(dados_feriados)

dias_acima_da_med = sum(f > med for f in dados_feriados)

print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Número de dias com dados acima da média mensal: {dias_acima_da_med}")
