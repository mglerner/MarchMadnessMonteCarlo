#!/usr/bin/env python

raise ImportError('Deprecated')
from __future__ import division
import numpy as np
import pylab as pl
from random import choice, shuffle
from numpy.random import random #import only one function from somewhere
from numpy.random import randint
from numpy import exp, array, zeros
import scipy
from time import sleep
from copy import deepcopy
from collections import Counter, OrderedDict

import RankingsAndStrength as RAS
import Visualization

import Brackets
from Brackets import Bracket
import Stats

from decorators import memoized




# now you can call deltaU(current_winner,current_loser) if you'd like.
#Brackets.deltaU = deltaU
#Brackets.energy_game = energy_game
#Brackets.energy_of_flipping = energy_of_flipping
