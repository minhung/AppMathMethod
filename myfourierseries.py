#!/usr/bin/env python

#
# http://stackoverflow.com/questions/20081866/generating-and-plotting-a-fourier-series-square-wave-in-python
#
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

list_ = []
phase = int(raw_input('Phase = '))
numofpts = 1000
#numofpts = int(raw_input('Number of points (>1000) = '))

x = np.linspace(0,25,numofpts) # grid of x data

def gen_list(phase): # Generating list of odd numbers for square wave function
    odd_phase = 0
    if phase % 2 == 0 and phase > 1: # If even phase
        odd_phase = phase - 1
        while odd_phase >= 0:
            list_.append(odd_phase)
            odd_phase = odd_phase - 2
    elif phase % 2 != 0 and phase > 1: # If odd phase
        odd_phase = phase
        while odd_phase >= 0:
            list_.append(odd_phase)
            odd_phase = odd_phase - 2
    elif phase == 1:
        odd_phase = phase
        list_.append(odd_phase)
    return list_


def add(x,phase): # The summation of the square wave function
    term = 0
    sum_ = 0
    complete = 0

    gen_list(phase)

    for k in list_:
        term = (1.0 / k) * np.sin( (k*x) / 2.0) 
        sum_ = term + sum_ 

    complete = 4.0/np.pi * sum_
    return complete

### Set up the initial data:
#phase = 25 # this variable will be controlled by slider

y = add(x,phase) # the function to plot       

### Set up the initial plot:
#ax = plt.subplot(111) # create new axes for 1 row, 1 column, plotnumber 1
#                  # This is the default axis
#plt.subplots_adjust(left=0.15, bottom=0.25) # make some more room at bottom and left
plt.line, = plt.plot(x, y, linewidth=1, color='r') # nb use of comma
plt.xlabel("x")
plt.ylabel("y(x)")

plt.show()