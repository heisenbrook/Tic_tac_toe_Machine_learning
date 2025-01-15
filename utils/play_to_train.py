from utils.board import check_triplets, action_train
from tqdm import tqdm

def play(player1, player2, turn):
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    for _ in tqdm(range(10000), 
                    desc='Training...', 
                    total=10000,
                    leave=True,
                    ncols=80):
        p_tot +=1

        while True:
            if turn == 1:
                action = action_train(player1, player2, turn, positions)
                positions[action-1] = 1
                turn = 2
                if check_triplets(positions) == True:
                    p1_win +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
                if check_triplets(positions) == 'Tie':
                    p_tie +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
            if turn == 2:
                action = action_train(player1, player2, turn, positions)
                positions[action-1] = 2
                turn = 1
                if check_triplets(positions) == True:
                    p2_win +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
                if check_triplets(positions) == 'Tie':
                    p_tie +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
                
    print('------------------')              
    print('Training finished!')  
    print(f'player1 wins {((p1_win/p_tot)*100):.2f} | player2 wins {((p2_win/p_tot)*100):.2f} | tie {((p_tie/p_tot)*100):.2f}')          
    
            