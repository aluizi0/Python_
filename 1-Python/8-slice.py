gameName = 'FreeFire'

gameDescription = '''
    Free Fire é um jogo eletrônico mobile de ação-aventura 
    do gênero battle royale, desenvolvido pela 111dots Studio
    e publicado pela Garena.
'''
#string[incio:fim] - indice comeca na posição 0
#indice final-1

print(gameName[0:]) # FreeFire

print(gameName[:4]) # Free

print(gameName[2:6]) # eeFir

#busca toda a string de 2 em 2 caracteres
print(gameName[::2]) # FeFr - pula de 2 em 2

#busca toda a string nos indices impares
print(gameName[1::2]) # reie - pula de 2 em 2

#inverte a string
print(gameName[::-1]) # eriFeerF