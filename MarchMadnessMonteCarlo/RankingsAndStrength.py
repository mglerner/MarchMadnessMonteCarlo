#!/usr/bin/env python
from __future__ import division
from collections import OrderedDict
from MarchMadnessMonteCarlo import KenPomeroy as KP
from MarchMadnessMonteCarlo import JeffSagarin as JS
from numpy.random import random #import only one function from somewhere

kenpom = {}
teams={}
teams['midwest'] = ['Kansas','UC Davis','Miami FL','Michigan St.',
                    'Iowa St.','Nevada','Purdue','Vermont',
                    'Creighton','Rhode Island','Oregon','Iona',
                    'Michigan','Oklahoma St.','Louisville','Jax. State']
teams['south'] = ['N. Carolina','Texas So.','Arkansas','Seton Hall',
                  'Minnesota','Middle Tenn.','Butler','Winthrop',
                  'Cincinnati','Kansas St.','UCLA','Kent St.',
                  'Dayton','Wichita St.','Kentucky','N. Kentucky']
teams['east'] = ['Villanova',"Mt St Mary's",'Wisconsin','Va. Tech',
                 'Virginia','UNC Wilm.','Florida','ETSU',
                 'SMU','USC','Baylor','New Mex. St.',
                 'S. Carolina','Marquette','Duke','Troy']
teams['west'] = ['Gonzaga','S. Dak. St.','Northwestern','Vanderbilt',
                 'Notre Dame','Princeton','W. Virginia','Bucknell',
                 'Maryland','Xavier','Florida St.','FGCU',
                 "St. Mary's", "VCU", "Arizona", 'North Dakota']

all_teams = teams['midwest'] + teams['south'] + teams['west'] + teams['east']

for strength_type in KP.lineparts:
    kenpom[strength_type] = {}
    for team in all_teams:
        try:
            kenpom[strength_type][team] = KP.kpomdata[team][strength_type]
        except KeyError:
            print("Can't find",team,"in",KP.kpomdata.keys())
            raise
