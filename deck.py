# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:54:55 2021

@author: 87118
"""
from card import *
import random



class Deck(object):
    
    def __init__(self):
        ''' build 卡组'''
        self.remain_cards =[]
        self.dead_cards =[]

        for rank in RANK_LIST:
            for suit in SUIT_LIST:
                c = Card(rank, suit)
                self.remain_cards.append(c)
        self.shuffle()
        
    def shuffle(self):
        ''' 打乱洗牌'''
        random.shuffle(self.remain_cards)
        
    def mix_card(self):
        ''' dead cards to remain_cards shuffle'''
        self.remain_cards = self.dead_cards
        self.dead_cards = []
        self.shuffle()
        
    def send_one_card_from_deck(self):
        '''飞出第一张牌 如果没了需要mix 洗牌'''
        if self.remain_cards:
            first_card = self.remain_cards[0]
            self.remain_cards.pop(0)
            return first_card
        else:
            self.mix_card()
            first_card = self.send_one_card_from_deck()
            return first_card
        
    def receive_dead_card(self, card):
        '''接受 卡牌 出牌'''
        self.dead_cards.append(card)
        