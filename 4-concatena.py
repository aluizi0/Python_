name = input("Digite o nome do jogo:")
yearLaunch = int(input("Digite o ano de lançamento do jogo:"))
gamePrice = float(input("Digite o preço do jogo:"))
planIncluded = input("Está incluso no serviço mensal?:")



print('##Dados do game##')
print('=================')

# Alternativa 1
# print('Nome do jogo:', name)
# print('Ano de lançamento:', yearLaunch)
# print('Preço do jogo:', gamePrice)
# print('Plano mensal incluso:', planIncluded)

# Alternativa 2
# print('Nome do jogo: ' + name, 
#       '\nAno de lançamento: ' + str(yearLaunch), 
#       '\nPreço do jogo: ' + str(gamePrice), 
#       '\nPlano mensal incluso: ' + planIncluded)

# Alternativa 3
print(f'Nome do jogo: {name}\nAno de lançamento: {yearLaunch}\nPreço do jogo: {gamePrice}\nPlano mensal incluso: {planIncluded}')