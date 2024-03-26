#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:03:53 2024

@author: fred
"""

#Welcome to Module 4 on Lists
x = [ 10, 20, 30, "hello"]
h = list(range(100))
h = h + [100] +[101,102]
maph = map(lambda a : a*a, h)
print"List of squares of odd numbers"
print(list(maph)[1:100:2])

def map(func, seq):
  new= []
  for item in seq:
    new += [func(item)]
  return new

def mapr (f, seq):
  if len(seq)== 0:
    return []
  else:
     return  mapr(f, seq[:-1]) + [f(seq[-1])]

def filter (pred, seq):
  new = []
  for item in seq:
    if pred(item):
      new += [item]
  return new

def filter_r (pred, seq):
  if len(seq) == 0:
    return []
  else:
    if pred(seq[0]):
      return [seq[0]] + filter_r(pred, seq[1:]
      )
    else: 
      return filter_r(pred, seq[1:])


h = list(range(1,11))
mh = mapr(lambda x: x*7, h)
mh == [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

fh= filter(lambda x: x%2 == 1, h)

pairs  =  [[1,2], [3,-3], [4,5]]
print(pairs[0][0])

def freq (val , seq):
  total = 0
  for i in seq:
    if i == val:
      total += 1
  return total

def freq_r (val,seq):
  if seq == []: #if len(seq)==0
    return 0
  else:
    if val == seq[0]:
      return 1 + freq_r(val, seq[1:])
    else:
      return freq_r(val,seq[1:])


def maplc(f, seq):
  return [f(i) for i in seq]

