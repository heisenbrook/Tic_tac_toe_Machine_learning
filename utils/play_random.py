import random
from tqdm import tqdm
import numpy as np
from utils.board import check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action

Q1 = {}


def action_r(Q, turn, positions):
    while True:
        if turn == 1:
            action = sel_e_greedy_action(Q, positions)
        if turn == 2:
            empty_pos = np.argwhere(positions == 0)
            action = random.choice(empty_pos)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play_r():
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    for _ in tqdm(range(10000000), 
                    desc='Training with random Q1', 
                    total=10000000,
                    leave=True,
                    ncols=80):
        
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_r(Q1, turn, positions)
                positions[action] = 1
                turn = 2      
            else:
                action = action_r(Q1, turn, positions)
                positions[action] = 2
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            update_q_table(Q1, cur_pos, action, 2, positions)
            positions = np.zeros(9)
            
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            update_q_table(Q1, cur_pos, action, 1, positions)
            positions = np.zeros(9)
            
        else:
            p2_win +=1
            update_q_table(Q1, cur_pos, action, -2, positions)
            positions = np.zeros(9)
            
        
    print('------------------')              
    print('Training Q1 finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')   
    


