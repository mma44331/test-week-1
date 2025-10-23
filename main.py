from game_logic.game import init_game,play_round

if __name__ == '__main__':
    players = init_game()
    p1 = players['player1']
    p2 = players['player2']
    while p1['hand'] and p2['hand']:
        play_round(players['player1'],players['player2'])
    if p1['wom_pile'] > p2['wom_pile']:
        print("the winner is" ,p1)
    else:
        print(("the winner is" ,p2))