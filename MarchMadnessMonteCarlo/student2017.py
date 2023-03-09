#!/usr/bin/env python
import csv
from numpy import matrix as mt
import numpy as np
from MarchMadnessMonteCarlo import RankingsAndStrength as RAS
kpr = RAS.kenpom['Rank']
adjo = RAS.kenpom['AdjO']
adjem = RAS.kenpom['AdjEM']
luck = RAS.kenpom['Luck']

rank_arr1 = [['1', 'Gonzaga', '32', '1', '97'],
 ['2', 'UCLA', '28', '3', '90.3'],
 ['2', 'Kansas', '28', '3', '90.3'],
 ['2', 'Villanova', '28', '3', '90.3'],
 ['5', 'Wichita St.', '30', '4', '88.2'],
 ['6', "St. Mary's", '28', '4', '87.5'],
 ['7', 'Arizona', '27', '4', '87.1'],
 ['7', 'Middle Tenn.', '27', '4', '87.1'],
 ['7', 'Cincinnati', '27', '4', '87.1'],
 ['7', 'SMU', '27', '4', '87.1'],
 ['7', 'Oregon', '27', '4', '87.1'],
 ['12', 'UNC Wilm.', '29', '5', '85.3'],
 ['13', 'Vermont', '28', '5', '84.8'],
 ['14', 'Kentucky', '26', '5', '83.9'],
 ['15', 'New Mex. St.', '25', '5', '83.3'],
 ['16', 'Monmouth', '27', '6', '81.8'],
 ['16', 'Illinois St.', '27', '6', '81.8'],
 ['18', 'Winthrop', '26', '6', '81.3'],
 ['18', 'N. Carolina', '26', '6', '81.3'],
 ['20', 'Purdue', '25', '6', '80.6'],
 ['20', 'Baylor', '25', '6', '80.6'],
 ['20', 'Nevada', '25', '6', '80.6'],
 ['23', 'Dayton', '24', '6', '80'],
 ['24', 'ETSU', '27', '7', '79.4'],
 ['25', 'FGCU', '26', '7', '78.8'],
 ['26', 'Belmont', '22', '6', '78.6'],
 ['27', 'Princeton', '21', '6', '77.8'],
 ['28', 'Maryland', '24', '7', '77.4'],
 ['28', 'W. Virginia', '24', '7', '77.4'],
 ['28', 'Akron', '24', '7', '77.4'],
 ['28', 'Louisville', '24', '7', '77.4'],
 ['28', 'Florida St.', '24', '7', '77.4'],
 ['28', 'Florida', '24', '7', '77.4'],
 ['28', 'UT Arlington', '24', '7', '77.4'],
 ['28', 'VCU', '24', '7', '77.4'],
 ['36', 'Butler', '23', '7', '76.7'],
 ['37', 'Bucknell', '26', '8', '76.5'],
 ['38', 'Oakland', '24', '8', '75'],
 ['38', 'Duke', '24', '8', '75'],
 ['38', 'Valparaiso', '24', '8', '75'],
 ['41', 'USC', '23', '8', '74.2'],
 ['41', 'Notre Dame', '23', '8', '74.2'],
 ['41', 'N.C. Cent', '23', '8', '74.2'],
 ['41', 'Arkansas', '23', '8', '74.2'],
 ['41', 'Wisconsin', '23', '8', '74.2'],
 ['41', 'Creighton', '23', '8', '74.2'],
 ['41', 'Minnesota', '23', '8', '74.2'],
 ['48', 'Col. of Charleston', '25', '9', '73.5'],
 ['48', 'UNCG', '25', '9', '73.5'],
 ['50', 'CSU Bakersfield', '21', '8', '72.4'],
 ['51', 'UNC Asheville', '23', '9', '71.9'],
 ['52', 'S. Carolina', '22', '9', '71'],
 ['52', 'Louisiana Tech', '22', '9', '71'],
 ['52', 'Virginia', '22', '9', '71'],
 ['52', 'Va. Tech', '22', '9', '71'],
 ['56', 'N. Kentucky', '24', '10', '70.6'],
 ['57', 'Houston', '21', '9', '70'],
 ['57', 'Rhode Island', '21', '9', '70'],
 ['59', 'Rice', '22', '10', '68.8'],
 ['60', 'North Dakota', '19', '9', '67.9'],
 ['61', 'Colorado St.', '21', '10', '67.7'],
 ['61', 'Eastern Wash.', '21', '10', '67.7'],
 ['61', 'Northwestern', '21', '10', '67.7'],
 ['61', 'Miami FL', '21', '10', '67.7'],
 ['65', 'BYU', '22', '11', '66.7'],
 ['65', 'South Dakota', '22', '11', '66.7'],
 ['65', 'Seton Hall', '20', '10', '66.7'],
 ['65', 'Utah', '20', '10', '66.7'],
 ['65', 'Iowa St.', '20', '10', '66.7'],
 ['65', 'UCF', '20', '10', '66.7'],
 ['65', 'Harvard', '18', '9', '66.7'],
 ['72', 'Louisiana', '21', '11', '65.6'],
 ['72', 'Furman', '21', '11', '65.6'],
 ['72', 'Texas So.', '21', '11', '65.6'],
 ['75', 'Boise St.', '19', '10', '65.5'],
 ['75', 'Ohio', '19', '10', '65.5'],
 ['75', 'A&M-Corpus Christi', '19', '10', '65.5'],
 ['78', 'Iona', '22', '12', '64.7'],
 ['79', 'Oklahoma St.', '20', '11', '64.5'],
 ['79', 'Ball St.', '20', '11', '64.5'],
 ['79', 'California', '20', '11', '64.5'],
 ['79', 'Providence', '20', '11', '64.5'],
 ['79', 'Michigan', '20', '11', '64.5'],
 ['84', 'UT Martin', '21', '12', '63.6'],
 ['84', 'Albany (NY)', '21', '12', '63.6'],
 ['86', 'Old Dominion', '19', '11', '63.3'],
 ['86', 'Marquette', '19', '11', '63.3'],
 ['86', 'Georgia St.', '19', '11', '63.3'],
 ['86', 'Fresno St.', '19', '11', '63.3'],
 ['86', 'Richmond', '19', '11', '63.3'],
 ['86', 'St. Bonaventure', '19', '11', '63.3'],
 ['86', 'North Dakota St.', '19', '11', '63.3'],
 ['93', 'Yale', '17', '10', '63'],
 ['94', 'Sam Houston St.', '20', '12', '62.5'],
 ['94', 'New Hampshire', '20', '12', '62.5'],
 ['94', 'Arkansas St.', '20', '12', '62.5'],
 ['94', 'San Francisco', '20', '12', '62.5'],
 ['94', 'Xavier', '20', '12', '62.5'],
 ['94', 'Wright St.', '20', '12', '62.5'],
 ['94', 'LIU Brooklyn', '20', '12', '62.5'],
 ['94', 'Lehigh', '20', '12', '62.5'],
 ['102', 'New Orleans', '18', '11', '62.1'],
 ['103', 'Chattanooga', '19', '12', '61.3'],
 ['103', 'Ole Miss', '19', '12', '61.3'],
 ['103', 'Memphis', '19', '12', '61.3'],
 ['103', 'UC Davis', '19', '12', '61.3'],
 ['103', 'Fort Wayne', '19', '12', '61.3'],
 ['103', 'George Mason', '19', '12', '61.3'],
 ['103', 'Kansas St.', '19', '12', '61.3'],
 ['110', 'Lipscomb', '20', '13', '60.6'],
 ['110', 'Towson', '20', '13', '60.6'],
 ['112', 'Texas St.', '18', '12', '60'],
 ['112', 'UMBC', '18', '12', '60'],
 ['114', "Saint Peter's", '19', '13', '59.4'],
 ['114', 'Wake Forest', '19', '13', '59.4'],
 ['114', 'Liberty', '19', '13', '59.4'],
 ['114', 'UC Irvine', '19', '13', '59.4'],
 ['114', 'Kent St.', '19', '13', '59.4'],
 ['114', 'Colorado', '19', '13', '59.4'],
 ['114', 'Lamar University', '19', '13', '59.4'],
 ['121', 'Jax. State', '20', '14', '58.8'],
 ['122', 'Idaho', '17', '12', '58.6'],
 ['122', 'Weber St.', '17', '12', '58.6'],
 ['122', 'Houston Baptist', '17', '12', '58.6'],
 ['125', 'Green Bay', '18', '13', '58.1'],
 ['125', 'Iowa', '18', '13', '58.1'],
 ['125', 'Illinois', '18', '13', '58.1'],
 ['125', 'Ga. Southern', '18', '13', '58.1'],
 ['125', 'Michigan St.', '18', '13', '58.1'],
 ["134","Troy","19","14","57.6"],
 ['153', "Mt St Mary's", "19", "15", "55.9"],
 ["154","Vanderbilt","17","14","54.8"],
 ["171","S. Dak. St.","18","16","52.9"],
]
rank_arr1 = np.array(rank_arr1)
#print(rank_arr1)
rank_arr2 = np.delete(rank_arr1, 1, axis=1)
rank_arr2 = rank_arr2.astype(np.float)
foul_arr=np.array(list(csv.reader(open("teams_fouls.csv","r"),delimiter=','))).astype('str')
foul_arr1 = np.delete(foul_arr, (0,1,2,3), axis=0)
foul_arr2 = np.delete(foul_arr1, range(355,368), axis=0)
#print(foul_arr)

def foul_decay(f1, f2):
    f1 = f1[4].astype(np.float)
    f2 = f2[4].astype(np.float)
    p = (200*200)/(team1*team2)
    foul_decay = np.exp(p)
    return foul_decay

anmol_map = {}
for (i,item) in enumerate(rank_arr1):
    anmol_map[item[1]] = i

def anmol_energy_game(winner, loser):
    team1 = rank_arr2[anmol_map[winner]]
    team2 = rank_arr2[anmol_map[loser]]
    diff= ((team1[0]*team1[1])/team1[2]) + ((team2[0]*team2[1])/team2[2])
    diff_norm = diff * ((team1[3]+team2[3])/200)
    inv_erg = abs(diff_norm)
    erg= np.exp(210/inv_erg)
    # weight somehow by better team
    erg = erg * team1[0]/team2[0]
#    erg = erg* foul_decay(team1,team2)   #modified erg
    return erg

def shengyao_energy_game(winner, loser):
    """My function for the energy of team A beating team B is E = ln
    (Rank A / Rank B).

    The rank of the team can be found on some sport analyst
    websites. If team A has a higher rank than team B, then Rank A /
    Rank B is a number smaller than 1, so the natural log of this
    number will give us a negative number. Conversely, if team A has a
    lower rank then team B, then Rank A/ Rank B will be bigger then 1,
    the energy of A beating B will be positive and will increase as
    the ratio of rank A and B increases.

    """
    result = np.log(kpr[winner]/kpr[loser])
    return result


def alex_energy_game(winner, loser):
    """def energy(A,B):
     get AdjEM ("adjusted efficiency margin," not the other AdjEMs) for A and B from kenpom.com
     energy = ln(AdjEM[A]/AdjEM[B])
    """
    result = np.log(adjem[loser]/adjem[winner])
    return result

def tyler_energy_game(winner, loser):
    """My energy function was defined as U=(Points scored per
    game/points opponent scored per game)(average assists/average
    turnovers). I did some back of a napkin calculations on the
    homework and this energy function seems to predict the better team
    will win more often and teams of equal skill will slightly favor
    the more defensive team. Is this kinda what you were looking
    for?
    """
    result = (adjo[winner]/adjo[loser])
    result = - result
    return result

def thad_energy_game(winner, loser):
    """Chance of team a + luck/ chance of team b plus its amount of luck>
    """
    result = (luck[winner] - luck[loser])
    result = - result
    return result

def atit_energy_game(winner, loser):
    result = 0
    return result

def sunil_energy_game(winner, loser):
    result = 0
    return result


def mujtaba_energy_game(winner, loser):
    result = 0
    return result
    

myrank =['Kansas',
         'UC Davis',
         'Miami FL',
         'Michigan St.',
         'Iowa St.',
         'Nevada',
         'Purdue',
         'Vermont',
         'Creighton',
         'Rhode Island',
         'Oregon',
         'Iona',
         'Michigan',
         'Oklahoma St.',
         'Louisville',
         'Jax. State',
         'N. Carolina',
         'Texas So.',
         'Arkansas',
         'Seton Hall',
         'Minnesota',
         'Middle Tenn.',
         'Butler',
         'Winthrop',
         'Cincinnati',
         'Kansas St.',
         'UCLA',
         'Kent St.',
         'Dayton',
         'Wichita St.',
         'Kentucky',
         'N. Kentucky',
         'Villanova',
         "Mt St Mary's",
         'Wisconsin',
         'Va. Tech',
         'Virginia',
         'UNC Wilm.',
         'Florida',
         'ETSU',
         'SMU',
         'USC',
         'Baylor',
         'New Mex. St.',
         'S. Carolina',
         'Marquette',
         'Duke',
         'Troy',
         'Gonzaga',
         'S. Dak. St.',
         'Northwestern',
         'Vanderbilt',
         'Notre Dame',
         'Princeton',
         'W. Virginia',
         'Bucknell',
         'Maryland',
         'Xavier',
         'Florida St.',
         'FGCU',
         "St. Mary's",
         "VCU",
         "Arizona",
         'North Dakota',
]

def rank_energy_game(winner,loser):
    result = myrank.index(winner)/myrank.index(loser)
    return result
