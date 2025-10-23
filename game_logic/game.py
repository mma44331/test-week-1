import random
from utils.deck import *

def create_player(name = "AI")->dict:
    start_game = {'name':name, 'hand':[],"wom_pile":[]}
    return start_game

def init_game()->dict:
    player1 = create_player("demy")
    player2 = create_player("")
    new_deck = create_deck()
    shuffle(new_deck)
    for i in new_deck[:26]:
        player1['hand'][i] = new_deck[i]
    for i in new_deck[26:]:
        player2['hand'][i] = new_deck[i]
    return {'deck':new_deck,'player1':player1,'player2':player2}
def play_round(p1:dict,p2:dict):
    card_player1 = p1['hand']
    p1['hand'].pop
    card_player2 = p2['hand']
    p1['hand'].pop
    winner = compare_cards(card_player1,card_player2)
    if winner == p1:
        p1['wom_pile'].append(card_player1)
        p1['wom_pile'].append(card_player2)
    if winner == p2:
        p2['wom_pile'].append(card_player1)
        p2['wom_pile'].append(card_player2)







