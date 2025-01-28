gameName = 'FreeFire'

gameDescription = '''
    Free Fire é um jogo eletrônico mobile de ação-aventura 
    do gênero battle royale, desenvolvido pela 111dots Studio
    e publicado pela Garena.
'''

print(gameName.upper()) # FREEFIRE
print(gameName.lower()) # freefire
print(gameName.capitalize()) # Freefire 1 letra maiuscula
print(gameName.title()) # Freefire 1 letra maiuscula
print(gameName.center(10, '-')) # FreeFire-- centraliza a string
print(gameName.find('Fire')) # 4 - retorna a posição da palavra Fire
print(gameDescription.count('Fire')) # 2 - conta quantas vezes a palavra Fire aparece na string
print(gameDescription.replace("Free Fire", "Pubg")) #Altera elementos
print(gameDescription.split(',')) # quebra a string em uma lista