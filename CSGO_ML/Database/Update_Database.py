from prettyprinter import pprint
from HLTV_data import *
import pandas as pd

matches = get_todays_matches()

#pprint(get_team_info(matches[1]['team1ID']))


def create_game(match):
    matchData = []
    teamA = get_team_info(matches[0]['team1ID'])
    teamB = get_team_info(matches[1]['team1ID'])


create_game(matches[0])
statistics = {'Team A: rank': [],
              'Team A: Amount players in top 30': [],
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
              'Team B: Amount players in top 30': [],
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
#df = pd.read_csv('Database/database.csv')
#df.loc[len(df.index)] = [0]
#df.to_csv('Database/database.csv')
