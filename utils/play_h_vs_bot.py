from utils.board import print_board, check_triplets
from utils.Q_player import sel_e_greedy_action
from utils.play_random import Q1

def action(turn, positions, epsilon):
    while True:
        if turn == 1:
            action = int(input('player 1, where to move? [1 to 9]:'))
            action -= 1
        if turn == 2:
            action = sel_e_greedy_action(Q1, positions, epsilon)
        if positions[action] == 0:
            return action
        else:
            print('spot already taken! please, choose a different spot on the board')
            continue
        
def play_h_vs_b(turn):
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    epsilon = 1

    while True:
        print_board(positions)
        if turn == 1:
            action = action(turn, positions, epsilon)
            positions[action] = 1
            turn = 2
            if check_triplets(positions) == True:
                print_board(positions)
                print('player1 wins!')
                positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
            if check_triplets(positions) == 'Tie':
                print_board(positions)
                print('Tie!')
                positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
        if turn == 2:
            action = action(turn, positions, epsilon)
            positions[action] = 2
            turn = 1
            if check_triplets(positions) == True:
                print_board(positions)
                print('player2 wins!')
                positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
            if check_triplets(positions) == 'Tie':
                print('Tie!')
                positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
            