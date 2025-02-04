import numpy as np
import random
from utils.play_random import Q1
from utils.board import check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action
from tqdm import tqdm


def action_train(Q, turn, positions):
    while True:
        if turn == 1:
            action = sel_e_greedy_action(Q, positions)
        if turn == 2:
            action = sel_e_greedy_action(Q, positions)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play():
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    for _ in tqdm(range(1000000), 
                    desc='Training...', 
                    total=1000000,
                    leave=True,
                    ncols=80):
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_train(Q1, turn, positions)
                positions[action] = 1
                update_q_table(Q1, cur_pos, action, 0, positions)
                turn = 2      
            else:
                action = action_train(Q1, turn, positions)
                positions[action] = 2
                update_q_table(Q1, cur_pos, action, 0, positions)
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            update_q_table(Q1, cur_pos, action, 1, positions)
            positions = np.zeros(9)
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            update_q_table(Q1, cur_pos, action, 0.5, positions)
            positions = np.zeros(9)
        else:
            p2_win +=1
            update_q_table(Q1, cur_pos, action, -2, positions)
            positions = np.zeros(9)
            
            
    outfile = open( 'Q1.txt', 'w' )
    for key in sorted(Q1):
        outfile.write( str(key) + '\t' + str(Q1[key]) + '\n' )
                
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} % | player2 wins {((p2_win/p_tot)*100):.2f} % | tie {((p_tie/p_tot)*100):.2f} %')

    
            