import random
from tqdm import tqdm
import numpy as np
from utils.board import print_board, check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action

Q1 = {}

def action_r(Q1, turn, positions, epsilon):
    while True:
        if turn == 1:
            action = sel_e_greedy_action(Q1, positions, epsilon)
        if turn == 2:
            action = random.randint(0,8)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play_r(turn):
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    epsilon = 0.5
    
    for _ in tqdm(range(100000), 
                    desc='Training...', 
                    total=100000,
                    leave=True,
                    ncols=80):
        p_tot +=1

        while True:
            cur_pos = positions.copy()
            if turn == 1:
                action = action_r(Q1, turn, positions, epsilon)
                positions[action] = 1
                turn = 2
                if check_triplets(positions) == True:
                    p1_win +=1
                    reward1 = 1
                    update_q_table(Q1, cur_pos, action, reward1, positions)
                    positions = np.zeros(9)
                    epsilon *= 0.99
                    break
                if check_triplets(positions) == 'Tie':
                    p_tie +=1
                    reward1 = 0.5
                    update_q_table(Q1, cur_pos, action, reward1, positions)
                    positions = np.zeros(9)
                    epsilon *= 0.99
                    break
                    
            if turn == 2:
                action = action_r(Q1, turn, positions, epsilon)
                positions[action] = 2
                turn = 1
                if check_triplets(positions) == True:
                    p2_win +=1
                    reward1 = 0
                    update_q_table(Q1, cur_pos, action, reward1, positions)
                    positions = np.zeros(9)
                    epsilon *= 0.99
                    break
                if check_triplets(positions) == 'Tie':
                    p_tie +=1
                    reward1 = 0.5
                    update_q_table(Q1, cur_pos, action, reward1, positions)
                    positions = np.zeros(9)
                    epsilon *= 0.99
                    break
                
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')   