from prettyprinter import pprint
from HLTV_data import *
from statistics import mean
import pandas as pd

matches = get_todays_matches()


def isolate_personal_player_data(team, dataType):
    lst = []
    players = team['playerStats']
    for player in players.keys():
        for j in players[player].keys():
            if j == dataType:
                lst.append(int(players[player][j]))
    return lst


def isolate_statistical_player_data(team, stat):
    lst = []
    players = team['playerStats']
    for player in players.keys():
        for j in players[player]['stats'].keys():
            if j == stat:
                lst.append(int(players[player]['stats'][j]))
    return lst


def create_game(match):
    matchData = []
    teamA = get_team_info(matches[0]['team1ID'])
    pprint(teamA)
    teamB = get_team_info(matches[1]['team1ID'])
    matchData.append(teamA['rank'])
    ages = isolate_personal_player_data(teamA, 'age')
    matchData.append(mean(ages))
    totalKills = isolate_statistical_player_data(teamA, 'total_kills')
    matchData.append(mean(totalKills))
    pprint(totalKills)
    pprint(mean(totalKills))



statistics = {'Team A: rank': [],
              'Team A: average age': [],
              'Team A: average total kills': [],
              'Team A: average headshot percentage': [],
              'Team A: average total deaths': [],
              'Team A: average KDR': [],
              'Team A: average damage per round': [],
              'Team A: average grenade damage per round': [],
              'Team A: average maps played': [],
              'Team A: average rounds played': [],
              'Team A: average kills per round': [],
              'Team A: assists per round': [],
              'Team A: average deaths per round': [],
              'Team A: average saved by teammates per round': [],
              'Team A: average saved teammates per round': [],
              'Team A: average rating': [],
              'Team B: rank': [],
              'Team B: average age': [],
              'Team B: average total kills': [],
              'Team B: average headshot percentage': [],
              'Team B: average total deaths': [],
              'Team B: average KDR': [],
              'Team B: average damage per round': [],
              'Team B: average grenade damage per round': [],
              'Team B: average maps played': [],
              'Team B: average rounds played': [],
              'Team B: average kills per round': [],
              'Team B: assists per round': [],
              'Team B: average deaths per round': [],
              'Team B: average saved by teammates per round': [],
              'Team B: average saved teammates per round': [],
              'Team B: average rating': [],
              'Outcome': []}
create_game(matches[0])
#df = pd.read_csv('Database/database.csv')
#df.loc[len(df.index)] = [0]
#df = pd.DataFrame(statistics)
#df.to_csv('database.csv')
