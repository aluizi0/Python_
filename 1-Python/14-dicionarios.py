gameFifa= {
    'name': 'Fifa 25',
    'yearLaunch': 2025,
    'gamePrice': 90.50,
    'classification': 8.5,
    'genre': ['esporte', 'família']
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperando um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscando apenas as chaves
print(gameFifa.keys())

# 3 - Buscando apenas os valores
print(gameFifa.values())

# 4 - Retorna itens do dicionário como tupla de uma lista 
print(gameFifa.items())

# 5 - Adicionando itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizando itens no dicionário
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Removendo item no dicionário
gameFifa.pop("players")
print(gameFifa)

