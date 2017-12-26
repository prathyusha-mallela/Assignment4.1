# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:47:42 2017

@author: Prathyusha Mallela
"""
#Assignment 4.1.1
def triangle_area(side1,side2,side3):
    S=(side1+side2+side3)/2
    A=((S*(S-side1)*(S-side2)*(S-side3)))**(0.5)
    return A
