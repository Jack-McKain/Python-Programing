#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:19:37 2024

@author: fred
"""

dict_example = {1: 'one', 2: 'two', 3: 'three'}

eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
#eng2sp['four']
v=eng2sp.values()
type(v) # <class 'dict_values'>
print(list(v)) # ['uno', 'dos', 'tres']
for k in eng2sp:
  print(k,"=>", eng2sp[k])
####################################################

def histogram(lst):
  """Returns a frequency table ftable as dict"""
  ftable={}
  for e in lst:
    if e not in ftable:
      ftable[e] = 1
    else:
      ftable[e] += 1
  return ftable

#print(histogram("parrot"))

quote="to be or not to be that is the question"

print(histogram(quote.split()))

url = "http://www.gutenberg.org/files/1533/1533-0.txt"

import os
from urllib.request import urlopen
shakes = urlopen(url)
shakestoken = shakes.read().decode('utf-8').split()

freq = histogram(shakestoken)

maxval= 0
bigword= ""
for word in freq:
  if freq[word] > maxval:
    bigword = word
    maxval = freq[word]

def successor(lst):
  succtable= {}
  for e in lst:
    succtable[e] = []

  prev = lst[0]
  for e in lst[1:]:
    if e not in succtable[prev]:
      succtable[prev] += [e]
    prev = e
  return succtable