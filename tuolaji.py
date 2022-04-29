# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:07:33 2021

@author: 87118


1000 ci 2人
count    1000.000000
mean       14.915000
std        15.265871
min         4.000000
25%         5.000000
50%         9.000000
75%        19.000000
max       130.000000
dtype: float64


100 run 5 ren
ounts.describe()
Out[37]: 
count    100.000000
mean      49.050000
std       24.697104
min       11.000000
25%       29.750000
50%       45.500000
75%       65.250000
max      133.000000
dtype: float64

100 run 4 ren
count    100.000000
mean      38.230000
std       24.659645
min        5.000000
25%       19.750000
50%       32.000000
75%       51.250000
max      108.000000
dtype: float64

"""




from deck import *
from la_strategy import *
import seaborn as sns
def player_turn(player_hand, last_card, last_suit, last_cards):
    ''' 根据上一张盘 行动 出牌或者 抽牌直到额能出'''
    if not player_hand: # 如果赢了空过
        return last_card, last_suit, player_hand, last_cards
    
    player_two_strate = La(player_hand, last_card, last_suit)
    action = player_two_strate.give_action()
    # print(action)
    if action == 'GIVE ONE':
        card_two, suit, player_hand = player_two_strate.give_card()
        last_cards.receive_dead_card(card_two)
        return card_two, suit, player_hand, last_cards

    else: # 抽牌
        new_card = last_cards.send_one_card_from_deck()
        print(f"draw {new_card}")
        player_hand.append(new_card)
        print(len(player_hand))
        card_two, suit, player_hand, last_cards = player_turn(player_hand, last_card, last_suit, last_cards)
        return card_two, suit, player_hand, last_cards


def run_one_time(player_num=2):
    # 洗盘
    cards = Deck()
    # print(cards.remain_cards[0])
    
    # 发牌
    # player_one = []
    # player_two = []

    players = [[] for i in range(player_num)]

    for i in range(5):
        for pl in players:
            pl.append(cards.send_one_card_from_deck())
        # player_one.append(cards.send_one_card_from_deck())
        # player_two.append(cards.send_one_card_from_deck())

        
    # 开始
    start = True
    count = 0
    have_people = 2

    while have_people >= 2:

    # while player_one and player_two:
        print(f"deck {len(cards.remain_cards)} deck {len(cards.dead_cards)} ")
        count += 1
        print(f"{count} rounds")
        if start:
            player_one = players[0]
            #player one
            player_one_strate = La(player_one, None, None)
            start = False
            card_out, suit_out, player_one = player_one_strate.give_card()
            # 加入目的
            cards.receive_dead_card(card_out)
            
            for pl in players[1:]:
                card_out, suit_out, pl, cards = player_turn(pl, card_out, suit_out, cards)

            # card_out, suit_out, player_two, cards = player_turn(player_two, card_one, suit, cards)
            continue
        # #first one
        # print("player one")
        # card_out, suit_out, player_one, cards = player_turn(player_one, card_out, suit_out, cards)
        # print("player two")
        # # # second one
        # card_out, suit_out, player_two, cards = player_turn(player_two, card_out, suit_out, cards)

        for pl in players:
            card_out, suit_out, pl, cards = player_turn(pl, card_out, suit_out, cards)
        have_people = 0
        for pl in players:
            if pl:
                have_people += 1
        print(f"people {have_people}")
    print(f"total nums {count}")
    return count        
if  __name__ == '__main__':
    counts = []
    for i in range(100):
        counts.append(run_one_time(4))
        
    counts = pd.Series(counts)
    counts.describe()
    sns.histplot(counts)
