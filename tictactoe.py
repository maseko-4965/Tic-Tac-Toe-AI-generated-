# Initialisation de la grille de jeu
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Affichage de la grille de jeu
def show_grid():
    for i in range(3):
        print('-------------')
        print(f'| {grid[i][0]} | {grid[i][1]} | {grid[i][2]} |')
    print('-------------')

# Vérification de la validité du coup
def is_valid_move(row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        print('Mouvement invalide. Les coordonnées doivent être entre 0 et 2.')
        return False
    elif grid[row][col] != ' ':
        print('Mouvement invalide. La case est déjà occupée.')
        return False
    else:
        return True

# Vérification de la fin de partie
def is_game_over():
    # Vérification des lignes
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ' ':
            print(f'Le joueur {grid[i][0]} a gagné !')
            return True
    # Vérification des colonnes
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ' ':
            print(f'Le joueur {grid[0][i]} a gagné !')
            return True
    # Vérification des diagonales
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        print(f'Le joueur {grid[0][0]} a gagné !')
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        print(f'Le joueur {grid[0][2]} a gagné !')
        return True
    # Vérification du match nul
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                return False
    print('Match nul !')
    return True

# Tour du joueur
def player_move(player):
    print(f'C\'est au joueur {player} de jouer.')
    row = int(input('Ligne (0-2) : '))
    col = int(input('Colonne (0-2) : '))
    if is_valid_move(row, col):
        grid[row][col] = player

# Boucle de jeu
def play_game():
    show_grid()
    while not is_game_over():
        player_move('X')
        show_grid()
        if is_game_over():
            break
        player_move('O')
        show_grid()

# Lancement du jeu
play_game()
