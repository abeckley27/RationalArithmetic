# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:54:33 2023

@author: Aidan Beckley
"""

import math

class fraction(object):

    def __init__(self, numer_, denom_ = 1):
       self.numer = numer_
       self.denom = denom_
    
    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    
    def __repr__(self):
        return str(self.numer) + "/" + str(self.denom)
    
    def reduce(self):
        gcf = math.gcd(int(self.numer), int(self.denom))
        self.numer //= gcf
        self.denom //= gcf
        
    def __mul__(self, frac2):
        
        output = fraction(int(self.numer * frac2.numer), int(self.denom * frac2.denom))
        output.reduce()
        return output
    
    def __add__(self, frac2):
        ansnum = (self.numer * frac2.denom) + (frac2.numer * self.denom)
        output = fraction(int(ansnum), int(self.denom * frac2.denom))
        output.reduce()
        return output
    
    def __sub__(self, frac2):
        ansnum = (self.numer * frac2.denom) - (frac2.numer * self.denom)
        output = fraction(ansnum, self.denom * frac2.denom)
        output.reduce()
        return output
    
    def __pow__(self, n):
        #Assuming n is an integer
        output = fraction(1)
        for i in range(n):
            output *= self
        return output
        
    def reciprocal(self):
        return fraction(self.denom, self.numer)
    
    def get_decimal(self):
        return self.numer / self.denom
    
    def __eq__(self, frac2):
        self.reduce()
        frac2.reduce()
        a = int(self.numer)
        b = int(self.denom)
        c = int(frac2.numer)
        d = int(frac2.denom)
        return (a == c) and (b == d)
    
    
    def __gt__(self, frac2):
        return self.get_decimal() > frac2.get_decimal()
    
    def __lt__(self, frac2):
        return self.get_decimal() < frac2.get_decimal()
    
    def __abs__(self):
        return fraction(abs(self.numer), abs(self.denom))
        
    
    













        
