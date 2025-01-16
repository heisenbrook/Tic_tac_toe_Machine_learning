import random
import numpy as np

from utils.board import check_triplets


def update_q_table(state, action, reward, new_state):
    old = Q[state][action]
    next_max = max(Q[new_state])
    Q[state][action] = (1 - alpha) * old + alpha * (reward + gamma * next_max) 
    
def sel_e_greedy_action(positions, eps):
    empty_pos = np.argwhere(positions == 0)
    if np.random.rand()  < eps or positions not in Q:
        action = tuple(random.choice(empty_pos))
        return action
    else:
        q_val = Q[positions]
        empty_q_val = [q_val[x[0], x[1]] for x in empty_pos]
        max_q_val = max(empty_q_val)
        max_q_ind = random.choice(np.argwhere(empty_q_val == max_q_val))
        action = tuple(empty_pos[max_q_ind]) 
        return action


alpha = 0.7
gamma = 0.01
epsilon = 0.82
discount = 0.99
num_episodes = 0
Q = {}

#main

def q_player(positions):
    positions = np.asarray(positions).reshape((3,3))


    epsilon = max(0.01, discount*epsilon)
