#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:05:22 2023

@author: fred
"""

# Week 2 - Higher Order Functions
# This week we will design a dispatch function using a registration process which returns a function that will apply dispatch

from operator import add, sub

print(add(2,3))
print(sub(2,3))
print(add(sub(2,3),add(2,3)))

def every(func, n):
 for i in range(1,n):
     print(func(i))

# # Apply func to every argument *arg allows 
# # variable number of arguments
def mymap (func, *args):
  f = lambda x: print(func(x))
  for a in args:  f(a)

s = lambda x: (x+x)
mymap(s, 10,20,30,35)

def f_depends_on_type_or_value(x,*args):
    if type(x) == str:
        # large block of code
        pass
    elif type(x) == int:
        # large block of code
        pass
    elif type(x) == float:
        # large block of code
        pass
    else:
        # some default large block of code
        pass


# #Cmd+/ or Cntl+/ to toggle comments

def register(status1, f1, status2, f2):
  def helper(status,arg):
    assert status == status1 or status == status2, "status Not Registered"
    if status == status1:
      return f1(arg)
    elif status == status2:
      return f2(arg)
  return helper

def mydispatch():
  def say_hello(name):
    return "Aloha " + name
  def say_bye(name):  
    return "Ciao " + name
  dispatch = register("Say Hi", say_hello,                  "Say Bye", say_bye)
  return dispatch

arglist = (("Say Hi", "Alonzo"),
            ("Say Bye", "Maria"), 
            ("No,no, register", "Bob"))

for a in arglist:
   print(mydispatch()(*a))

