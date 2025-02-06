# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla
gamesTuple = ('gta','freefire','pes 25','fifa 25','mortal kombat')
print(gamesTuple)
print(type(gamesTuple))

# Busque os dois primeiros itens da lista
print(gamesTuple[0:2])

# Busque o último item da lista
print(gamesTuple[-1])

# Busca jogos até uma posição
print(gamesTuple[:3])

# Busca jogos de uma posição em diante
print(gamesTuple[2:])

# Recupera um item da tupla pelo índice
print(gamesTuple.index("freefire"))