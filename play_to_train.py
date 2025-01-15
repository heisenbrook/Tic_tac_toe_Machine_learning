from utils.Q_player import player1, player2
from utils.board import print_board, check_triplets, action_train

print('which one should start first?')
turn = int(input('[1/2]:'))

def play(player1, player2, turn):
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    p1_win, p2_win, p_tie, p_tot = 0, 0, 0, 0
    
    while p_tot <= 10000:
        p_tot +=1

        while True:
            print_board()
            if turn == 1:
                action = action_train(player1, player2, turn, positions)
                positions[action] = 1
                turn = 2
                if check_triplets() == True:
                    p1_win +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
            if turn == 2:
                action = action_train(player1, player2, turn, positions)
                positions[action] = 2
                turn = 1
                if check_triplets() == True:
                    p2_win +=1
                    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    break
            if check_triplets() == 'Tie':
                p_tie +=1
                positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                break
            