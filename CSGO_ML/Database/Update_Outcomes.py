from prettyprinter import pprint
from HLTV_data import *
import pandas as pd

def get_team_names(match):
    teamA = match['team1'].decode("utf-8")
    teamB = match['team2'].decode("utf-8")
    result = teamA + ' v ' + teamB
    return result


def get_outcome(result):
    return result['team1score']-result['team2score']


def update_outcomes(df, results):
    for result in results:
        teamNames = get_team_names(result)

        for rowIndex, row in df.iterrows():
            if teamNames == df.at[rowIndex, 'Team Names']:
                if df.at[rowIndex, 'Outcome'] == 'undefined':
                    df.at[rowIndex, 'Outcome'] = get_outcome(result)


df = pd.read_csv('database.csv')
update_outcomes(df, get_todays_results())
df.to_csv('database.csv', index=False)
