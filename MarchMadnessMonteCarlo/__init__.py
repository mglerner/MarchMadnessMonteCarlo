"""
This is March Madness Monte Carlo code, originally written by Michael Lerner
and described on his [blog](http://www.mglerner.com/blog/?p=16), then modified
by Daniel Smith and posted to
[github](https://github.com/Daniel-B-Smith/MarchMadnessMonteCarlo) and forked
back by Michael Lerner on his own
[github](https://github.com/mglerner/MarchMadnessMonteCarlo) project.

Check out the blog post for a nice summary.
"""

__version__ = 0.3

from . import config

from numpy.random import random #import only one function from somewhere
#from Brackets import *
#from Stats import *
#from JeffSagarin import *
#from KenPomeroy import *
#from Stats import *
#from MonteCarloBrackets import simulate
#from RankingsAndStrength import *
#from RankingsAndStrength import teams


# These are for use externally (i.e. by driver scripts or notebooks)
from .teams import Teams, Regions, All_teams
from .Brackets import Bracket, simulate, runbracket1, runbracket2, playgame, maketable
from .Visualization import showstats
set_energy_function = config.set_energy_function
import examples
#from .examples import default_energy_game
set_energy_function(examples.default_energy_game)
