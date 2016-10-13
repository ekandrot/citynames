# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:23:26 2016

@author: Edward Kandrot
"""

import random

def findnthList(xs, r):
    for c, w in enumerate(xs):
        r -= w
        if r < 0:
            return chr(ord('A') + c)
    return 'z'

def findnthDict(xs, r):
    for k in xs:
        if k != 'total':
            w = xs[k]
            r -= w
            if r < 0:
                return k
    return '*'

cities = []
with open("US_Cities.txt") as f:
    for line in f:
        cities.append(line)

firstLetter = [0]*26
secondLetter = {}  # treat second letter dictionary separately
combos2 = {}  # generates one letter from another, ie 2 letters in dict
combos3 = {}  # generates one letterr from two letters, ie 3 letters in dict
for city in cities:
    letter = city[0]
    firstLetter[ord(letter)-ord('A')] += 1

    prevLetter = letter
    letter = city[1]
    dict0 = secondLetter.get(prevLetter, {})
    dict0[letter] = dict0.get(letter, 0) + 1
    secondLetter[prevLetter] = dict0
    
    prevLetter = letter
    for letter in city[2:]:
        dict0 = combos2.get(prevLetter, {})
        dict0[letter] = dict0.get(letter, 0) + 1
        combos2[prevLetter] = dict0
        prevLetter = letter

    prevLetter0 = city[0]
    prevLetter1 = city[1]
    for letter in city[2:]:
        prevCombo = prevLetter0 + prevLetter1
        dict0 = combos3.get(prevCombo, {})
        dict0[letter] = dict0.get(letter, 0) + 1
        combos3[prevCombo] = dict0
        prevLetter0, prevLetter1 = prevLetter1, letter


for k in secondLetter:
    d = secondLetter[k]
    t = 0
    for c in d:
        t += d[c]
    d['total'] = t

for k in combos2:
    d = combos2[k]
    t = 0
    for c in d:
        t += d[c]
    d['total'] = t

for k in combos3:
    d = combos3[k]
    t = 0
    for c in d:
        t += d[c]
    d['total'] = t


total = len(cities)

def generate_with_combos2():
    for i in range(20):
        word = ''
        r = int(random.uniform(0, total-1))
        letter = findnthList(firstLetter, r)
        word += letter
    
        r = int(random.uniform(0, secondLetter[letter]['total']-1))
        letter = findnthDict(secondLetter[letter], r)
        word += letter
    
        while letter != '\n':
            r = int(random.uniform(0, combos2[letter]['total']-1))
            letter = findnthDict(combos2[letter], r)
            if letter == '\n':
                break
            word += letter
        print(word)
        
def generate_with_combos3():
    for i in range(20):
        word = ''
        r = int(random.uniform(0, total-1))
        letter = findnthList(firstLetter, r)
        word += letter
        prevLetter0 = letter
    
        r = int(random.uniform(0, secondLetter[letter]['total']-1))
        letter = findnthDict(secondLetter[letter], r)
        word += letter
        prevLetter1 = letter
    
        while letter != '\n':
            prevCombo = prevLetter0 + prevLetter1
            r = int(random.uniform(0, combos3[prevCombo]['total']-1))
            letter = findnthDict(combos3[prevCombo], r)
            if letter == '\n':
                break
            word += letter
            prevLetter0, prevLetter1 = prevLetter1, letter
        print(word)

print("--- Generate with two combos ---")
generate_with_combos2()
print("--- Generate with three combos ---")
generate_with_combos3()
