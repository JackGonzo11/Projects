from prettyprinter import pprint
from HLTV_data import *
import pandas as pd

"""
get all results
for each result:
    find team names
    put the outcome into the row
"""

def update_outcomes(df, results):
    for col_name, data in df.items():
        print("col_name:", col_name, "\ndata:", data)


df = pd.read_csv('database.csv')
update_outcomes(df, get_results())
#pprint(get_results())
#results = get_results()
