#!/usr/bin/env python

import RankingsAndStrength as RAS
import teams
regional_rankings = teams.regional_rankings

strength = RAS.kenpom['AdjEM']

def default_energy_game(winner, loser):
    """This is where you'll input your own energy functions. Here are
    some of the things we talked about in class. Remember that you
    want the energy of an "expected" outcome to be lower than that of
    an upset.

    """
    result = -(strength[winner] - strength[loser])
    result = regional_rankings[winner] - regional_rankings[loser]
    result = regional_rankings[winner]/regional_rankings[loser]
    result = -(strength[winner]/strength[loser])
    result = -(strength[winner]-strength[loser])/200.0
    #result = random()
    #result = color of team 1 jersey better than color of team 2 jersey
    #print "energy_game(",winner,loser,")",result
    return result

def log5_energy_game(winner, loser):
    strength = RAS.kenpom['Pyth']
    A,B = strength[winner],strength[loser]
    # see http://207.56.97.150/articles/playoff2002.htm
    win_pct = (A-A*B)/(A+B-2*A*B)
    return -win_pct
