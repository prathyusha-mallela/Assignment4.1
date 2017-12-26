# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:11:57 2017

@author: Prathyusha Mallela
"""

#Assignment 4.1.2
def longest_word_list(txt,n):
    #longest_word_list
    wordlist = []
    for item in txt:
        if len(item) > n:
            continue
        wordlist.append(item)
    return wordlist

lst=['a','ab','abc','abcd','abcde','ghyhghbibujbhjohniohniohn']
wrdl=longest_word_list(lst,4)
#wrdl