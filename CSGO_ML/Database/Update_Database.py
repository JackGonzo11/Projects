from prettyprinter import pprint
from HLTV_data import *
from statistics import mean
from datetime import date
import pandas as pd
import time

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
                num = players[player]['stats'][j]
                if len(num) > 4 and num[4] == '%':
                    lst.append(float(num[0:4]))
                else:
                    try:
                        lst.append(int(num))
                    except ValueError:
                        lst.append(float(num))
    return lst


def get_team_names(match):
    teamA = match['team1'].decode("utf-8")
    teamB = match['team2'].decode("utf-8")
    result = teamA + ' v ' + teamB
    pprint(result + ' grabbed')
    return result


def create_game(match):
    matchData = []
    teamA = get_team_info(match['team1ID'])
    teamB = get_team_info(match['team2ID'])

    matchData.append(date.today())

    matchData.append(get_team_names(match))

    matchData.append(teamA['rank'])

    ages = isolate_personal_player_data(teamA, 'age')
    matchData.append(mean(ages))

    totalKills = isolate_statistical_player_data(teamA, 'total_kills')
    matchData.append(mean(totalKills))

    hspercentage = isolate_statistical_player_data(teamA, 'headshot_percent')
    matchData.append(mean(hspercentage))

    totalDeaths = isolate_statistical_player_data(teamA, 'total_deaths')
    matchData.append(mean(totalDeaths))

    kdr = isolate_statistical_player_data(teamA, 'kd_ratio')
    matchData.append(mean(kdr))

    damage = isolate_statistical_player_data(teamA, 'dmg_per_round')
    matchData.append(mean(damage))

    grenadeDmg = isolate_statistical_player_data(teamA, 'grenade_dmg_per_round')
    matchData.append(mean(grenadeDmg))

    mapsPlayed = isolate_statistical_player_data(teamA, 'maps_played')
    matchData.append(mean(mapsPlayed))

    roundsPlayed = isolate_statistical_player_data(teamA, 'rounds_played')
    matchData.append(mean(roundsPlayed))

    killsPerRound = isolate_statistical_player_data(teamA, 'kills_per_round')
    matchData.append(mean(killsPerRound))

    assistsPerRound = isolate_statistical_player_data(teamA, 'assists_per_round')
    matchData.append(mean(assistsPerRound))

    deathsPerRound = isolate_statistical_player_data(teamA, 'deaths_per_round')
    matchData.append(mean(deathsPerRound))

    savedByTeam = isolate_statistical_player_data(teamA, 'saved_by_teammate_per_round')
    matchData.append(mean(savedByTeam))

    savedTeam = isolate_statistical_player_data(teamA, 'saved_teammates_per_round')
    matchData.append(mean(savedTeam))

    rating = isolate_statistical_player_data(teamA, 'rating_1')
    matchData.append(mean(rating))

    matchData.append(teamB['rank'])

    ages = isolate_personal_player_data(teamB, 'age')
    matchData.append(mean(ages))

    totalKills = isolate_statistical_player_data(teamB, 'total_kills')
    matchData.append(mean(totalKills))

    hspercentage = isolate_statistical_player_data(teamB, 'headshot_percent')
    matchData.append(mean(hspercentage))

    totalDeaths = isolate_statistical_player_data(teamB, 'total_deaths')
    matchData.append(mean(totalDeaths))

    kdr = isolate_statistical_player_data(teamB, 'kd_ratio')
    matchData.append(mean(kdr))

    damage = isolate_statistical_player_data(teamB, 'dmg_per_round')
    matchData.append(mean(damage))

    grenadeDmg = isolate_statistical_player_data(teamB, 'grenade_dmg_per_round')
    matchData.append(mean(grenadeDmg))

    mapsPlayed = isolate_statistical_player_data(teamB, 'maps_played')
    matchData.append(mean(mapsPlayed))

    roundsPlayed = isolate_statistical_player_data(teamB, 'rounds_played')
    matchData.append(mean(roundsPlayed))

    killsPerRound = isolate_statistical_player_data(teamB, 'kills_per_round')
    matchData.append(mean(killsPerRound))

    assistsPerRound = isolate_statistical_player_data(teamB, 'assists_per_round')
    matchData.append(mean(assistsPerRound))

    deathsPerRound = isolate_statistical_player_data(teamB, 'deaths_per_round')
    matchData.append(mean(deathsPerRound))

    savedByTeam = isolate_statistical_player_data(teamB, 'saved_by_teammate_per_round')
    matchData.append(mean(savedByTeam))

    savedTeam = isolate_statistical_player_data(teamB, 'saved_teammates_per_round')
    matchData.append(mean(savedTeam))

    rating = isolate_statistical_player_data(teamB, 'rating_1')
    matchData.append(mean(rating))

    matchData.append('undefined')
    print("adding game to database")

    return matchData

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

def update_database(db):
    matches = get_todays_matches()
    for match in matches:
        matchData = create_game(match)
        db.loc[len(df.index)] = matchData
        db.to_csv('database.csv', index=False)
        print("added game")

df = pd.read_csv('database.csv')
update_database(df)
#df = pd.DataFrame(statistics)

print("database update complete")
