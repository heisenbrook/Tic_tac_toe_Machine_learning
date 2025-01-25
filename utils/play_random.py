import random
from tqdm import tqdm
import numpy as np
from utils.play_to_train import Q1, Q2
from utils.board import check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action


def action_r(Q, turn, positions, epsilon):
    while True:
        if turn == 1:
            action = sel_e_greedy_action(Q, positions, epsilon)
        if turn == 2:
            action = random.randint(0,8)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play_r():
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    epsilon = 0.5
    
    for _ in tqdm(range(100000), 
                    desc='Training with random Q1', 
                    total=100000,
                    leave=True,
                    ncols=80):
        
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_r(Q1, turn, positions, epsilon)
                positions[action] = 1
                update_q_table(Q1, cur_pos, action, 0, positions)
                turn = 2      
            else:
                action = action_r(Q1, turn, positions, epsilon)
                positions[action] = 2
                update_q_table(Q1, cur_pos, action, 0, positions)
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            update_q_table(Q1, cur_pos, action, 1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            update_q_table(Q1, cur_pos, action, 0.5, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        else:
            p2_win +=1
            update_q_table(Q1, cur_pos, action, -1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        
    print('------------------')              
    print('Training Q1 finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')   
    
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    epsilon = 0.5
        
    for _ in tqdm(range(100000), 
                    desc='Training with random Q2', 
                    total=100000,
                    leave=True,
                    ncols=80):
        
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_r(Q2, turn, positions, epsilon)
                positions[action] = 1
                update_q_table(Q2, cur_pos, action, 0, positions)
                turn = 2      
            else:
                action = action_r(Q2, turn, positions, epsilon)
                positions[action] = 2
                update_q_table(Q2, cur_pos, action, 0, positions)
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            update_q_table(Q2, cur_pos, action, 1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            update_q_table(Q2, cur_pos, action, 0.5, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        else:
            p2_win +=1
            update_q_table(Q2, cur_pos, action, -1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
                
    print('------------------')              
    print('Training Q2 finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')  
    
    outfile = open( 'Q1.txt', 'w' )
    for key in sorted(Q1):
        outfile.write( str(key) + '\t' + str(Q1[key]) + '\n' )
        
    outfile1 = open( 'Q2.txt', 'w' )
    for key in sorted(Q2):
        outfile1.write( str(key) + '\t' + str(Q2[key]) + '\n' ) 