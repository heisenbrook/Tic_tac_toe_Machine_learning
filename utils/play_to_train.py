import numpy as np
import random
from utils.board import check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action
from tqdm import tqdm

Q1 = {}
Q2 = {}

def action_train(Q1, Q2, turn, positions, epsilon):
    while True:
        if turn == 1:
            action = sel_e_greedy_action(Q1, positions, epsilon)
        if turn == 2:
            action = sel_e_greedy_action(Q2, positions, epsilon)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play():
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    epsilon = 0.5
    
    for _ in tqdm(range(300000), 
                    desc='Training...', 
                    total=300000,
                    leave=True,
                    ncols=80):
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_train(Q1, Q2, turn, positions, epsilon)
                positions[action] = 1
                update_q_table(Q1, cur_pos, action, 0, positions)
                turn = 2      
            else:
                action = action_train(Q1, Q2, turn, positions, epsilon)
                positions[action] = 2
                update_q_table(Q2, cur_pos, action, 0, positions)
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            update_q_table(Q1, cur_pos, action, 1, positions)
            update_q_table(Q2, cur_pos, action, -1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            update_q_table(Q1, cur_pos, action, 0.5, positions)
            update_q_table(Q2, cur_pos, action, 0.5, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
        else:
            p2_win +=1
            update_q_table(Q1, cur_pos, action, -1, positions)
            update_q_table(Q2, cur_pos, action, 1, positions)
            positions = np.zeros(9)
            epsilon *= 0.99
                
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')
    

    
            