#!/usr/bin/env python
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from random import choice, shuffle
from numpy.random import random #import only one function from somewhere
from numpy.random import randint
from numpy import exp, array, zeros, ones, convolve
import scipy
from time import sleep
from copy import deepcopy
from collections import Counter, OrderedDict


def movingaverage(interval, window_size):
    window= ones(int(window_size))/float(window_size)
    return convolve(interval, window, 'same')

def plotone(brackets, label, subplot1, subplot2, values=None, label2=None, 
            values2=None, description=None, useavg=False):
    """
    Plotting too many points causes lots of trouble for matplotlib. At
    the moment, we deal with that by plotting at most 50000 points,
    skipping evenly through the data if needed.
    """
    maxpts = 50000

    ntrials = len(brackets)
    if values is None:
        try:
            values = [getattr(b,label)() for b in brackets]
        except TypeError:
            values = [getattr(b,label) for b in brackets]

    if len(values) >= 50000:
        step = divmod(len(values),maxpts)[0]
    else:
        step = 1
    plt.subplot(subplot1)
    plt.plot(range(0,ntrials,step),values[::step],'.',label=label)
    if useavg:
        # want something like 2000 windows
        if step > 1:
            npts = maxpts
        else:
            npts = len(values)
        avgstep = divmod(len(values),int(npts/25))[0]
        
        plt.plot(range(0,ntrials,step),movingaverage(values[::step],avgstep),'-',label='avg. '+label)
            
    plt.ylabel(label.capitalize())
    plt.xlabel('Game')
    if description is not None:
        plt.title('%s over the trajectory, T=%s, %s'%(label.capitalize(),
                                                     brackets[0].T,description))
    else:
        plt.title('%s over the trajectory, T=%s'%(label.capitalize(),
                                                 brackets[0].T))
    #plt.legend()
    plt.subplot(subplot2)
    if values2 is None:
        if ntrials > 1000:
            nbins = min(int(ntrials/100),200)
        else:
            nbins = 10
        plt.hist(values,bins=nbins)
        plt.title('%s distribution, T=%s'%(label.capitalize(), brackets[0].T))
    else:
        plt.subplot(subplot2)
        plt.plot(range(0,ntrials,step),values2[::step],'.',label=label2)
        plt.ylabel(label2.capitalize())
        plt.xlabel('Game')
        plt.title('%s over the trajectory, T=%s'%(label2.capitalize(),
                                                 brackets[0].T))

    
def showstats(sr,newfig=False,description='MMMC',figsize=(15,8)):
    if newfig:
        plt.figure(figsize=figsize)
    plotone(sr.brackets, 'energy', 231, 234, description=description)
    plotone(sr.brackets, 'upsets', 232, 235, description=description)
    plotone(sr.brackets, 'Unique brackets', 233, 236, values=sr.unique_brackets,
            label2="Lowest Energy Sightings", values2=sr.lowest_bracket_count,
            description=description)
    plt.show()
