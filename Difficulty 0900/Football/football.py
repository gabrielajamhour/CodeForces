all_players = input()

players_consecutivos = 1 # É inicializada uma variável para contar sequências consecutivas de players
player_anterior = all_players[0] # Nos permite comparar o caractere atual com o caractere anterior
found = False # Essa variável nos ajudará a determinar se encontramos uma subsequência de 7 players do mesmo time


for player_atual in all_players:
    if player_atual == player_anterior:
        players_consecutivos += 1
        if players_consecutivos >= 7:
            found = True
            break
    else:
        players_consecutivos = 1
        player_anterior = player_atual

if found:
    print("YES")
else:
    print("NO")
