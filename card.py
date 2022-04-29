# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:49:08 2021

@author: 87118
"""
RANK_LIST = [i for i in range(2, 15)]
SUIT_LIST = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
class Card(object):
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.check()
    
    def check(self):
        if self.rank not in RANK_LIST:
            print(f"wrong rank {self.rank}")
        if self.suit not in SUIT_LIST:
            print(f"wrong suit {self.suit}")
        
    def __str__(self):
        return f"{self.rank}{self.suit}"