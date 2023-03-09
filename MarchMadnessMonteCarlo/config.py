#!/usr/bin/env python

from collections import namedtuple

date = 2017

default_energy_function = None
def set_energy_function(ef):
    global default_energy_function
    default_energy_function = ef

SimulationResults = namedtuple('SimulationResults','brackets unique_brackets lowest_bracket lowest_bracket_count most_common_bracket most_common_bracket_count')
    
