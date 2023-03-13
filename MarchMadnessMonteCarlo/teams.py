#!/usr/bin/env python

from . import config
from numpy.random import random #import only one function from somewhere
from numpy.random import randint

# These should probably be teams not Teams. But I was having weird import errors.
# a file in this directory would say `from . import teams as _teams` and then the
# _teams they would get was the teams dict here. Changing this to upper case fixed the
# problem.
Teams = {}
if config.date == 2013:
    Teams['midwest'] = ['Louisville','North Carolina A&T','Colorado St.','Missouri',
                        'Oklahoma St.','Oregon','St. Louis','New Mexico St.',
                        'Memphis',"St. Mary's",'Michigan St.','Valparaiso',
                        'Creighton','Cincinnati','Duke','Albany']

    #Could be La Salle instead of Boise St.
    Teams['west'] = ['Gonzaga','Southern','Pittsburgh','Wichita St.',
                     'Wisconsin','Mississippi','Kansas St.','La Salle',
                     'Arizona','Belmont','New Mexico','Harvard',
                     'Notre Dame','Iowa St.','Ohio St.','Iona']

    Teams['south'] = ['Kansas','Western Kentucky','North Carolina','Villanova',
                      'Virginia Commonwealth','Akron','Michigan','South Dakota St.',
                      'UCLA','Minnesota','Florida','Northwestern St.',
                      'San Diego St.','Oklahoma','Georgetown','Florida Gulf Coast']

    # Could be Long Island instead of James Madison
    Teams['east'] = ['Indiana','James Madison','North Carolina St.','Temple',
                     'Nevada Las Vegas','California','Syracuse','Montana',
                     'Butler','Bucknell','Marquette','Davidson',
                     'Illinois','Colorado','Miami FL','Pacific']
elif config.date == 2015:
    Teams['midwest'] = ['Kentucky','Hampton','Cincinnati','Purdue',
                        'West Virginia','Buffalo','Maryland','Valparaiso',
                        'Butler','Texas','Notre Dame','Northeastern',
                        'Wichita St.','Indiana','Kansas','New Mexico St.']
    # Could be MISS instead of BYU
    Teams['west'] = ['Wisconsin','Coastal Carolina','Oregon','Oklahoma St.',
                     'Arkansas','Wofford','North Carolina','Harvard',
                     'Xavier','Mississippi','Baylor','Georgia St.',
                     'VCU','Ohio St.','Arizona','Texas Southern',
                     ]
    # Could be Boise State instead of Dayton
    Teams['east'] = ['Villanova','Lafayette','North Carolina St.','LSU',
                     'Northern Iowa','Wyoming','Louisville','UC Irvine',
                     'Providence','Dayton','Oklahoma','Albany',
                     'Michigan St.','Georgia','Virginia','Belmont']
    # Could be University of North Florida instead of Robert Morris
    Teams['south'] = ['Duke','Robert Morris','San Diego St.',"St. John's",
                      'Utah','Stephen F. Austin','Georgetown','Eastern Washington',
                      'SMU','UCLA','Iowa St.','UAB',
                      'Iowa','Davidson','Gonzaga','North Dakota St.']
elif config.date == 2017:
    Teams['midwest'] = ['Kansas','UC Davis','Miami FL','Michigan St.',
                        'Iowa St.','Nevada','Purdue','Vermont',
                        'Creighton','Rhode Island','Oregon','Iona',
                        'Michigan','Oklahoma St.','Louisville','Jax. State']
    Teams['south'] = ['N. Carolina','Texas So.','Arkansas','Seton Hall',
                      'Minnesota','Middle Tenn.','Butler','Winthrop',
                      'Cincinnati','Kansas St.','UCLA','Kent St.',
                      'Dayton','Wichita St.','Kentucky','N. Kentucky']
    Teams['east'] = ['Villanova',"Mt St Mary's",'Wisconsin','Va. Tech',
                     'Virginia','UNC Wilm.','Florida','ETSU',
                     'SMU','USC','Baylor','New Mex. St.',
                     'S. Carolina','Marquette','Duke','Troy']
    Teams['west'] = ['Gonzaga','S. Dak. St.','Northwestern','Vanderbilt',
                     'Notre Dame','Princeton','W. Virginia','Bucknell',
                     'Maryland','Xavier','Florida St.','FGCU',
                     "St. Mary's", "VCU", "Arizona", 'North Dakota']
elif config.date == 2023:
    # The ones to check on:
    # Pittsburgh
    # Arizona St.
    # Texas Southern 
    Teams['midwest'] = ['Houston','Northern Kentucky','Iowa','Auburn',
                        'Miami FL','Drake','Indiana','Kent St.',
                        'Iowa St.','Pittsburgh','Xavier','Kennesaw St.',
                        'Texas A&M','Penn St.','Texas','Colgate']
    Teams['south'] = ['Alabama','Texas A&M Corpus Chris','Maryland','West Virginia',
                      'San Diego St.','Charleston','Virginia','Furman',
                      'Creighton','N.C. State','Baylor','UC Santa Barbara',
                      'Missouri','Utah St.','Arizona','Princeton']
    Teams['east'] = ['Purdue','Texas Southern','Memphis','Florida Atlantic',
                     'Duke','Oral Roberts','Tennessee','Louisiana',
                     'Kentucky','Providence','Kansas St.','Montana St.',
                     'Michigan St.','USC','Marquette','Vermont']
    Teams['west'] = ['Kansas','Howard','Arkansas','Illinois',
                     "Saint Mary's",'VCU','Connecticut','Iona',
                     'TCU','Arizona St.','Gonzaga','Grand Canyon',
                     "Northwestern", "Boise St.", "UCLA", 'UNC Asheville']
else:
    raise ImportError('Unknown bracket date: {v}'.format(v=config.date))

# These are all listed in the same order:
_rankings = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
Regional_rankings = {}
for region in Teams:
    for (team,rank) in zip(Teams[region],_rankings):
        # We use a random number here so that the south's number 2
        # seed won't come out exactly the same rank as the west's.
        Regional_rankings[team] = rank + random()/10

Regions = {}
for region in Teams:
    for team in Teams[region]:
        Regions[team] = region

All_teams = Teams['midwest'] + Teams['south'] + Teams['west'] + Teams['east']

Teams['all'] = All_teams
