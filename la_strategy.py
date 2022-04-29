# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:08:10 2021

@author: 87118
"""

import pandas as pd

class La(object):
    ''' 拉 黄包车 '''
    def __init__(self, card_list, last_card, last_suit):
        self.card_list = card_list
        self.last_card = last_card
        self.available_card_list = []
        self.j_index = False
        
        if last_card is None:
            return None
        # build information according to strategy that give cards that you have 
        # by order, if have j and others doing other cards
        suits = []
        for idx, card in enumerate(self.card_list):
            if self.available_card(card, self.last_card, last_suit):
                if card.rank == 11:
                    self.j_index = idx
                self.available_card_list.append(idx)
            # 统计花色 遂作
            if card.rank != 11:
                suits.append(card.suit)
        if suits:
            suits = pd.Series(suits)
            self.most_suit = suits.value_counts().index[0]
        else:
            self.most_suit = card_list[0].suit
            
                    
        
    def available_card(self,card_a, card_b, last_suit):
        '''card a 手牌 card b 场上牌 '''
        ok = False
        # 是否为j
        if card_a.rank == 11:
            ok = True
        elif card_a.rank == card_b.rank:
            ok = True
        elif card_a.suit == last_suit:
            ok = True
        return ok
    
    def give_action(self):
        '''根据 available_card_list 做决定'''
        if self.available_card_list:
            return "GIVE ONE"
        return "DRAW"

    def give_card(self):
        ''' 出牌
        card, suit, cards after deleteone'''
        if self.last_card is None:
            idx = 0
            out_card = self.card_list[idx]
            self.card_list.pop(idx)
            print(out_card, "out", "first time")
            return out_card, out_card.suit, self.card_list

        
        if len(self.available_card_list) > 1 and self.j_index:
            for idx in self.available_card_list:
                if idx != self.j_index:
                    out_card = self.card_list[idx]
                    self.card_list.pop(idx)
                    print(out_card, "out", "have j and others")
                    return out_card, out_card.suit, self.card_list
        if self.j_index:
            out_card = self.card_list[self.j_index]
            self.card_list.pop(self.j_index)
            print(out_card, "out", "j", "change suit", self.most_suit)

            return out_card, self.most_suit, self.card_list
        
        idx = self.available_card_list[0]
        out_card = self.card_list[idx]
        self.card_list.pop(idx)
        print(out_card, "out", "first one")
        return out_card, out_card.suit, self.card_list
     
             