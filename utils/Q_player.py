import random
import numpy as np

def update_q_table(Q, state, action, reward, new_state):
    alpha = 0.7
    gamma = 0.01
    state = str(state)
    new_state = str(new_state)
    q_values = Q.get(state, np.zeros(9))
    next_q_values = Q.get(new_state, np.zeros(9))
    max_next_q_value = np.max(next_q_values)
    q_values[action] += alpha * (reward + gamma * max_next_q_value - q_values[action])

    Q[state] = q_values
    
def sel_e_greedy_action(Q, positions, epsilon):
    str_positions = str(positions)
    empty_pos = np.argwhere(positions == 0)
    if np.random.rand()  < epsilon or str_positions not in Q:
        action = random.choice(empty_pos)
        return action
    else:
        q_val = Q[str_positions]
        empty_q_val = [q_val[x[0]] for x in empty_pos]
        max_q_val = max(empty_q_val)
        max_q_ind = random.choice([i for i in range(len(empty_pos)) if empty_q_val[i] == max_q_val])
        action = empty_pos[max_q_ind] 
        return action





