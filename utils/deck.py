import random
def create_card(rank:str,suite:str) -> dict:
    card_dict = {}
    card_dict['rank'] = rank
    card_dict['suite'] = suite
    if rank > 0 and rank < 11:
        card_dict['value'] = rank
    else:
        if rank == "J":
            card_dict['value'] = "11"
        if rank == "Q":
            card_dict['value'] = "12"
        if rank == "K":
            card_dict['value'] = "13"
        else:
            card_dict['value'] = "14"
    return card_dict


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card['value'] == p2_card['value']:
        return "WAR"
    if p1_card['value'] > p2_card['value']:
        return "p1"
    return "p2"


def create_deck() -> list[dict]:
    card_deck = []
    suite_list = ["h","c","d","s"]
    rank_list = ["J","Q","K","A"]
    for suite in suite_list:
        for item in rank_list:
            if item == "J":
                new_dard_deck = create_card(item,suite)
                card_deck.append(new_dard_deck)
            elif item == "Q":
                new_dard_deck = create_card(item,suite)
                card_deck.append(new_dard_deck)
            elif item == "K":
                new_dard_deck =create_card(item,suite)
                card_deck.append(new_dard_deck)
            else:
                new_dard_deck = create_card(item,suite)
                card_deck.append(new_dard_deck)
    return card_deck


def shuffle(deck:list[dict]) -> list[dict]:
    for i in range(1000):
        while True:
            index1 = random.randint(0,51)
            index2 = random.randint(0,51)
            if index1 != index2:break
        deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck

