from utils.play_h_vs_h import play_h
from utils.play_to_train import play
from utils.play_random import play_r
from utils.play_h_vs_bot import play_h_vs_b

print('which one should start first?')
turn = int(input('[1/2]:'))

#play_h(turn)
play(turn)
play_r(turn)
play_h_vs_b(turn)