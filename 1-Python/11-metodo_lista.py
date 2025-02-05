gamesList = ['Valorant', 'Lolzin', 'Pes 25', 'cod', 'fortnite', 'freefire']

# 1 - Tamanho da lista
print(f'O tamanho da sua biblioteca de Jogos é: {len(gamesList)}')

# 2 - Recupera um item da lista pelo índice
print(f'Seu Jogo esta no index: {gamesList.index('Pes 25')}')

# 3 - Adiciona item ao final da lista
gamesList.append("Gta V")
print(f'Opa! Você acabou de adicionar o jogo: {gamesList}, à sua biblioteca!')

# 4 - Ordena lista
gamesList.sort()
print(f'Sua biblioteca de jogos na ordem! ==> {gamesList}')

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Pes 25')
gamesReset.remove('cod')
print(f'Sua biblioteca copiada, sem dois jogos: {gamesReset}')

# 6 - Remove todos os itens da lista
gamesList.clear()
print(f'Sua biblioteca foi esvaziada: {gamesList}')