def play(player1, player2, turn=False):
    positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    while True:
        if turn:
            action = int(input('player 1, where to move? [1 to 9]:'))
            if positions[action] == 0:
                positions[action] = 1
            else:
                print('spot already taken! please, choose a different spot on the board')
                continue
        else:
            action = int(input('player 2, where to move? [1 to 9]:'))
            if positions[action] == 0:
                positions[action] = 2
            else:
                print('spot already taken! please, choose a different spot on the board')
                continue