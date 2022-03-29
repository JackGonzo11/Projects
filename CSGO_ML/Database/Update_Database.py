from prettyprinter import pprint
from Database.HLTV_data import *

matches = get_todays_matches()


pprint(get_team_info(matches[0]['team1ID']))
