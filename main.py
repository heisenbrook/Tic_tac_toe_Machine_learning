from utils.play_h_vs_h import play_h
from utils.play_to_train import play
from utils.play_random import play_r
from utils.play_h_vs_bot import play_h_vs_b



#play_h(turn)


play()

#play_r()



p_again = 'y'

while p_again == 'y':
    print('You are player 1! which one should start first?')
    turn = int(input('[1/2]:'))
    play_h_vs_b(turn)
    p_again = input('would you like to play again? [y/n]:')