import numpy as np
import random
from utils.play_random import Q1
from utils.board import check_triplets
from utils.Q_player import update_q_table, sel_e_greedy_action
from utils.DQN_player import select_action, update_model, model, loss_fn
from collections import deque
from tqdm import tqdm


def action_train(Q, positions):
    while True:
        action = sel_e_greedy_action(Q, positions)
        if positions[action] == 0:
            return action
        else:
            continue
        
def play():
    num_episodes = 1000000
    positions = np.zeros(9)
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    for _ in tqdm(range(num_episodes), 
                    desc='Training...', 
                    total=num_episodes,
                    leave=True,
                    ncols=80):
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_train(Q1, positions)
                positions[action] = 1
                turn = 2      
            else:
                action = action_train(Q1, positions)
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
            
            
    outfile = open( 'Q1.txt', 'w' )
    for key in sorted(Q1):
        outfile.write( str(key) + '\t' + str(Q1[key]) + '\n' )
                
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} % | player2 wins {((p2_win/p_tot)*100):.2f} % | tie {((p_tie/p_tot)*100):.2f} %')

    
def action_train_dqn(positions, memory, epsilon, cur_pos, batch_size):
    while True:
        action = select_action(positions, epsilon)
        if positions[action] == 0:
            return action
        else:
            memory.append((cur_pos, action, -3, positions, False))
            if len(memory) > batch_size:
                update_model(memory, batch_size)
            continue
    

        
def play_dqn():
    num_episodes = 100000
    batch_size = 32
    memory = deque(maxlen=num_episodes*10)
    positions = np.zeros(9)
    epsilon = 0.9
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    for _ in tqdm(range(num_episodes), 
                    desc='Training DQN...', 
                    total=num_episodes,
                    leave=True,
                    ncols=80):
        p_tot +=1
        
        turn = random.randint(1,2)

        while check_triplets(positions) == False :
            cur_pos = positions.copy()
            if turn == 1:
                action = action_train_dqn(positions, memory, epsilon, cur_pos, batch_size)
                positions[action] = 1
                memory.append((cur_pos, action, 0, positions, False))
                turn = 2      
            else:
                action = action_train_dqn(positions, memory, epsilon, cur_pos, batch_size)
                positions[action] = 2
                memory.append((cur_pos, action, 0, positions, False))
                turn = 1
        
        if check_triplets(positions) == True and turn == 2:
            p1_win +=1
            memory.append((cur_pos, action, 2, positions, True))
            if len(memory) > batch_size:
                update_model(memory, batch_size)
                epsilon *= 0.99
            positions = np.zeros(9)
        elif check_triplets(positions) == 'Tie':
            p_tie +=1
            memory.append((cur_pos, action, 1, positions, True))
            if len(memory) > batch_size:
                update_model(memory, batch_size)
                epsilon *= 0.99
            positions = np.zeros(9)
        else:
            p2_win +=1
            memory.append((cur_pos, action, -2, positions, True))
            if len(memory) > batch_size:
                update_model(memory, batch_size)
                epsilon *= 0.99
            positions = np.zeros(9)
                            
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} % | player2 wins {((p2_win/p_tot)*100):.2f} % | tie {((p_tie/p_tot)*100):.2f} %')
            