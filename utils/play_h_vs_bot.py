import numpy as np
from utils.board import print_board, check_triplets
from utils.Q_player import sel_e_greedy_action
from utils.play_random import Q1

def act(turn, positions, epsilon):
    while True:
        if turn == 1:
            action = int(input('player 1, where to move? [0 to 8]:'))
        if turn == 2:
            action = sel_e_greedy_action(Q1, positions, epsilon)
        if positions[action] == 0:
            return action
        else:
            print('spot already taken! please, choose a different spot on the board')
            continue
        
def play_h_vs_b(turn):
    positions = np.zeros(9)
    epsilon = 0

    while check_triplets(positions) == False :
        print_board(positions)
        if turn == 1:
            action = act(turn, positions, epsilon)
            positions[action] = 1
            turn = 2      
        else:
            action = act(turn, positions, epsilon)
            positions[action] = 2
            turn = 1
        
    if check_triplets(positions) == True and turn == 1:
        print_board(positions)
        print('player1 wins!')
        positions = np.zeros(9)
    elif check_triplets(positions) == 'Tie':
        print_board(positions)
        print('Tie!')
        positions = np.zeros(9)
    else:
        print_board(positions)
        print('player2 wins!')
        positions = np.zeros(9)
            