#!/usr/bin/env python
from __future__ import division
import numpy as np
import pylab as pl
from random import choice,shuffle
from numpy.random import random #import only one function from somewhere
from numpy.random import randint
from numpy import exp,array,zeros,inf
import scipy
from time import sleep
from copy import deepcopy
from collections import Counter, OrderedDict, defaultdict
#from decorators import memoized
from . import config
from . import teams as _teams
from . import RankingsAndStrength as RAS
from . import Visualization
from .config import SimulationResults
#from MarchMadnessMonteCarlo import Stats

regional_rankings = _teams.Regional_rankings
#strength = RAS.kenpom['Luck']
#strength = RAS.sagarin['Rating']
#strength = RAS.kenpom['Pyth']
strength = RAS.kenpom['AdjEM']

#T = 0.5 # In units of epsilon/k
#T = 2.5 # In units of epsilon/k


#@memoized
def energy_of_flipping(current_winner, current_loser):
    """Given the current winner and the current loser, this calculates
    the energy of swapping, i.e. having the current winner lose.
    """
    return (config.default_energy_function(current_loser, current_winner) - 
            config.default_energy_function(current_winner, current_loser))

deltaU = energy_of_flipping

# Here are the "magic functions" I mentioned to get pairs of teams.
from itertools import zip_longest
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def pairs(iterable):
    return grouper(2,iterable)



def playgame(team1, team2, T):
    """There's a difference between flipping a game in an existing
    bracket, and playing a game from scratch. If we're going to just
    use Boltzmann statistics to play a game from scratch, we can make
    life easy by using the Boltzmann factor to directly pick a
    winner.

    """
    ediff = deltaU(team1, team2)
    boltzmann_factor = exp(-ediff/T)

    win_prob = boltzmann_factor/(1+boltzmann_factor) if boltzmann_factor < inf else 1
    # So, prob of team 1 winning is then boltzmann_factor/(1+boltzmann_factor)
    if random() >= win_prob:
        return (team1,team2)
    else:
        return (team2,team1)

def playgamesfortesting(team1, team2, ntrials, T):
    print("Boltzmann tells that the ratio of team1 winning to team 2"+ 
          "winning should be")
    print(exp(-deltaU(team1,team2)/T))
    wins = {team1:0,team2:0}
    for i in range(ntrials):
        winner,loser = playgame(team1,team2,T)
        wins[winner] = wins[winner] + 1
    print("wins {} {} {} {} {}".format(wins, wins[team1]/wins[team2], 
                                       wins[team2]/wins[team1], 
                                       wins[team1]/ntrials, 
                                       wins[team2]/ntrials))

def playround(teams, T):
    winners = []
    losers = []
    for (team1, team2) in pairs(teams):
        winner, loser = playgame(team1,team2,T)
        winners.append(winner)
        losers.append(loser)
    return winners,losers

    
def runbracket(teams, T):
    # How many rounds do we need?
    nrounds = int(np.log2(len(teams)))
    winners = teams #they won to get here!
    all_winners = [winners]
    for round in range(nrounds):
        winners, losers = playround(winners, T)
        all_winners.append(winners)
    return all_winners


def bracket_energy(all_winners):
    total_energy = 0.0
    for i in range(len(all_winners)-1):
        games = pairs(all_winners[i])
        winners = all_winners[i+1]
        for (team1, team2),winner in zip(games, winners):
            if winner == team1:
                total_energy += config.default_energy_function(team1, team2)
            else:
                total_energy += config.default_energy_function(team2, team1)
    return total_energy

def getroundmap(bracket, include_game_number):
    games_in_rounds = [2**i for i in reversed(range(len(bracket)-1))]
    round = {}
    g = 0
    for (i,gir) in enumerate(games_in_rounds):
        for j in range(gir):
            if include_game_number:
                round[g] = (i,j)
            else:
                round[g] = i
            g += 1
    return round

#@profile
def simulate(ntrials, region, T, printonswap=False, printbrackets=True):
    """
    If region is "west" "midwest" "south" or "east" we'll run a bracket based 
    just on those teams.
    If it's "all" we'll run a full bracket.
    If it's a list of teams, we'll run a bracket based just on that list.

    So, one way you might want to do things is to simulate 10000 runs for each 
    of the four brackets,
    then run your final four explicitly, e.g.

    T = 1.5
    simulate(10000,'midwest',T)
    # record results
    simulate(10000,'south',T)
    # record results
    simulate(10000,'west',T)
    # record results
    simulate(10000,'east',T)
    # record results

    simulate(10000,['Louisville','Kansas','Wisconsin','Indiana'],T)
    """

    if type(region)  in (type([]), type(())):
        teams = region[:]
    else:
        teams = _teams.Teams[region]
    b = Bracket(teams, T)
    energy = b.energy()
    ng = sum(b.games_in_rounds) # total number of games
    # Let's collect some statistics
    brackets = []
    for trial in range(ntrials):
        g = randint(0, ng) # choose a random game to swap
        #print "attempted swap for game",g#,"in round",round[g]
        #newbracket = deepcopy(b)
        newbracket = b.copy()
        newbracket.swap(g)
        newenergy = newbracket.energy()
        ediff = newenergy - energy
        if ediff <= 0:
            b = newbracket
            energy = newenergy
            if printonswap:
                print("LOWER")
                print(b)
        else:
            if random() < exp(-ediff/T):
                b = newbracket
                energy = newenergy
                if printonswap:
                    print( "HIGHER")
                    print(b)
        brackets.append(b)


    lb, mcb, mcb_count, unique_brackets, lowest_sightings = \
        Stats.gather_uniquestats(brackets)
    sr = SimulationResults(brackets,unique_brackets,lb,lowest_sightings,mcb,mcb_count)
    if printbrackets:
        print("Lowest energy bracket")
        print(lb)
        print("Most common bracket (%s)"%mcb_count)
        print(mcb)
    return sr

def runbracket1(ntrials, T):
    results = {'all':simulate(ntrials,'all',T)}
    return results

def runbracket2(ntrials1, ntrials2, T):
    results = {}
    regions = 'midwest west south east'.split()
    for (i,region) in enumerate(regions):
        results[region] = simulate(ntrials1, region, T, printbrackets=False)
    # Make a new bracket from our final four
    teams = [results[region].most_common_bracket.bracket[-1][0] for region in regions]
#    ff_lb, ff_mcb, ff_mcb_count = simulate(ntrials2, teams, T, newfig=i+1, 
    ff_sr = simulate(ntrials2, teams, T, printbrackets=False)

    print("YOUR LOWEST ENERGY BRACKETS")
    for region in regions:
        print("LOWEST ENERGY BRACKET FOR REGION", region)
        print(results[region].lowest_bracket)
        print()
    print( "LOWEST ENERGY BRACKET FOR FINAL FOUR")
    print( ff_sr.lowest_bracket)
        
    print( "YOUR MOST COMMON BRACKETS")
    for region in regions:
        print("MOST COMMON BRACKET FOR REGION", region)
        print(results[region].most_common_bracket)
        print("number of times this bracket happened:",results[region].most_common_bracket_count)
        print()
        print()
    print( "MOST COMMON BRACKET FOR FINAL FOUR")
    print( ff_sr.most_common_bracket)
    print( "number of times this bracket happened:",ff_sr.most_common_bracket_count)
    results['final four'] = ff_sr
    return results


class Bracket(object):
    def __init__(self, teams, T, bracket=None):
        """
        
        Arguments:
        - `teams`:
        - `T`:
        """
        self.teams = teams
        self.T = T
        if bracket is None:
            self.bracket = runbracket(self.teams, self.T)
        else:
            self.bracket = bracket
        self.games_in_rounds = [2**i for i in 
                                reversed(range(len(self.bracket)-1))]
        self.roundmap = getroundmap(self.bracket, include_game_number=False)
        self.roundmap_with_game_numbers = getroundmap(self.bracket, 
                                                      include_game_number=True)
    def copy(self):
        return self.__class__(self.teams, self.T,  
                              bracket=[l[:] for l in self.bracket])
    def energy(self):
        return bracket_energy(self.bracket)
    def __str__(self):
        return bracket_to_string(self.bracket)
    __repr__ = __str__
    def __hash__(self):
        return hash(tuple([tuple(aw) for aw in self.bracket]))
    def game(self, g):
        """Return (team1,team2,winner).
        """
        t1, t2, win = self._getgameidxs(g)
        return (self.bracket[t1[0]][t1[1]], self.bracket[t2[0]][t2[1]],
                self.bracket[win[0]][win[1]])

    def _round_teaminround_to_game(self,r,gir):
        return sum(self.games_in_rounds[:r]) + int(gir/2)

    def _getgameidxs(self, g):
        # we'll return (round,game) for each of team1, team2, winner
        # 0 1 2 3 4 5 6 7 # teams 1
        # 0 0 1 1 2 2 3 3 # games 1
        # 0 2 4 6 # teams 2
        # 0 0 1 1 # games 2
        round, game_in_round = self.roundmap_with_game_numbers[g]
        return ((round,2*game_in_round), (round,2*game_in_round+1), 
                (round+1,game_in_round))
    def _setwinner(self, g, winner):
        """ JUST SETS THE WINNER, DOES NOT LOOK TO NEXT ROUND! USE SWAP FOR 
        THAT! 
        """
        t1,t2,win = self._getgameidxs(g)
        self.bracket[win[0]][win[1]] = winner
    def swap(self, g):
        """
        NOTE: This does not check 
        """
        team1, team2, winner = self.game(g)
        if team1 == winner:
            self._setwinner(g, team2)
        else:
            self._setwinner(g, team1)
        wr, wt = self._getgameidxs(g)[2]
        ng = self._round_teaminround_to_game(wr, wt)
        while ng < sum(self.games_in_rounds):
            #print "Now need to check game",wr,wt,ng,self.game(ng)
            winner, loser = playgame(self.game(ng)[0], self.game(ng)[1], self.T)
            self._setwinner(ng, winner)
            wr, wt = self._getgameidxs(ng)[2]
            ng = self._round_teaminround_to_game(wr, wt)
    def upsets(self):
        result = 0
        for g in range(sum(self.games_in_rounds)):
            t1,t2,win = self.game(g)
            if t1 == win:
                los = t2
            else:
                los = t1
            if energy_of_flipping(win,los) < 0:
                result += 1
        return result

def bracket_to_string(all_winners):
    """ Cute version that prints out brackets for 2, 4, 8, 16, 32, 64, etc. """
    result = ''
    aw = all_winners # save some typing later
    nrounds = len(all_winners) #int(np.log2(len(teams)))
    # We'll keep the results in a big array it turns out that arrays
    # of strings have to know the max string size, otherwise things
    # will just get truncated.
    maxlen = max([len(s) for s in all_winners[0]])
    dt = np.dtype([('name', np.str_, maxlen)])
    results = array([['' for i in range(len(all_winners[0]))] for j in 
                     range(nrounds)], dtype=dt['name'])
    # First round, all of the spots are filled
    results[0] = all_winners[0]
    # all other rounds, we split the row in half and fill from the middle out.
    for i in range(1, nrounds): # we've done the 1st and last already
        # round 1 skips two, round 2 skips 4, etc.
        these_winners = all_winners[i]
        # Fill top half
        idx = int(len(all_winners[0])/2 - 1)
        for team in reversed(all_winners[i][:int(len(all_winners[i])/2)]):
            results[i][idx] = team
            idx -= 2**i
        # Fill bottom half
        idx = int(len(all_winners[0])/2)
        for team in all_winners[i][int(len(all_winners[i])/2):]:
            results[i][idx] = team
            idx += 2**i

    def tr(i,include_rank=False,maxlen=None):
        """ Print out the team and ranking """
        if maxlen is not None:
            team = i[:maxlen]
        else:
            team = i
        if include_rank:
            try:
                region = _teams.Regions[i]
                result = '%s (%s)'%(team,int(_teams.Regional_rankings[i]))
            except KeyError:
                result = '%s'%(team)
        return result
    stub = '%-25s ' + ' '.join(['%-8s']*(nrounds-1))
    for i in range(len(all_winners[0])):
        these = results[:,i]
        these = [tr(these[0], include_rank=True)] + \
            [tr(i, maxlen=3, include_rank=True) for i in these[1:]]
        result += stub % tuple(these)
        result += '\n'
    result += "Total bracket energy: %s"%bracket_energy(all_winners)
    result += '\n'
    return result

def print_bracket(bracket):
    print( bracket_to_string(bracket))


def makehtmltable(tabledata,headers):
    result = '<table>\n'
    result += '<tr>'
    for header in headers:
        result += '<th>{h}</th>'.format(h=header)
    result += '</tr>\n'
    for row in tabledata:
        result += '<tr>'
        for col in row:
            result += '<td>{c}</td>'.format(c=col)
        result += '</tr>\n'
    result += '</table>'
    return result

class Stats:
    @staticmethod
    def gather_uniquestats(brackets):
        lb = Bracket(brackets[0].teams, T=0.0000001) # low bracket
        low_hash = hash(lb)
        cnt = Counter()
        unique_brackets = []
        lowest_sightings = []
        brackets_by_hash = {}
        for b in brackets:
            h = hash(b)
            cnt[h] += 1
            unique_brackets.append(len(cnt))
            lowest_sightings.append(cnt[low_hash])
            brackets_by_hash[h] = b
        h,c = cnt.most_common(1)[0]
        mcb = brackets_by_hash[h] # most comon bracket
        return lb, mcb, c, unique_brackets, lowest_sightings

    @staticmethod
    def maketable(results):
        counts = defaultdict(Counter)
        allrounds = ['2nd Round','3rd Round','Sweet 16','Elite 8','Final 4','Championship','Win']
        rounds1 = ['2nd Round','3rd Round','Sweet 16','Elite 8','Final 4']
        rounds2 = ['Championship','Win']
        if 'all' not in results:
            for region in 'south midwest east west'.split():
                for bracket in results[region].brackets:
                    for (name,num) in zip(rounds1,[0,1,2,3,4]):
                        for team in bracket.bracket[num]:
                            counts[team][name] += 1
            for bracket in results['final four'].brackets:
                for (name,num) in zip(rounds2,[1,2]):
                    for team in bracket.bracket[num]:
                        counts[team][name] += 1
            nt1 = len(results['south'].brackets)
            nt2 = len(results['final four'].brackets)
        else:
            for bracket in results['all'].brackets:
                for (name,num) in zip(allrounds,[0,1,2,3,4,5,6]):
                    for team in bracket.bracket[num]:
                        counts[team][name] += 1
            nt1 = nt2 = len(results['all'].brackets)
        # Now turn that into percentages
        pct = {}
        for team in counts:
            pct[team] = {}
            for r in ['2nd Round','3rd Round','Sweet 16','Elite 8','Final 4']:
                pct[team][r] = 100*counts[team][r]/nt1
            for r in ['Championship','Win']:
                pct[team][r] = 100*counts[team][r]/nt2
            pct[team]['Region'] = _teams.Regions[team]
            pct[team]['Rank'] = int(_teams.Regional_rankings[team])
        def tablekey(d):
            # gets teamname, pct
            return [d[1][i] for i in reversed(allrounds)]
        items = reversed(sorted(pct.items(),key=tablekey))
        # make a table
        headers = ['Team'] + ['Region','Rank'] + allrounds
        tabledata = []
        for (team,pcts) in items:
            tabledata.append([team] + [pcts[i] for i in ['Region','Rank'] + allrounds])
        #return tabulate(tabledata, headers=headers, tablefmt="html" )
        return makehtmltable(tabledata, headers=headers)
maketable = Stats.maketable
