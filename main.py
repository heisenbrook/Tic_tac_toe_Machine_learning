from utils.play_to_train import play, play_dqn
from utils.play_random import play_r
from utils.play_h_vs_bot import play_h_vs_q, play_vs_dqn 




#play_r()

#play()

play_dqn()


p_again = 'y'

while p_again == 'y':
    print('You are player 1! which one should start first?')
    turn = int(input('[1/2]:'))
    play_vs_dqn(turn)
    p_again = input('would you like to play again? [y/n]:')