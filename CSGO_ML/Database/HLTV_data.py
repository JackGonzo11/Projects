import re
import time

from prettyprinter import pprint
import requests
import datetime
import arrow
from bs4 import BeautifulSoup
from python_utils import converters
from datetime import date

def get_parsed_page(url):
    # This fixes a blocked by cloudflare error i've encountered
    headers = {
        "referer": "https://www.hltv.org/stats",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    webpage = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")
    ## this could break at some point
    while len(webpage) == 7:
        print("cloudflare blocked request, waiting 90 seconds")
        time.sleep(90)
        print("trying again")
        webpage = BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

    return webpage


def top5teams():
    home = get_parsed_page("http://hltv.org/")
    count = 0
    teams = []
    for team in home.find_all("div", {"class": ["col-box rank"], }):
        count += 1
        teamname = team.text[3:]
        teams.append(teamname)
    return teams


def top30teams():
    page = get_parsed_page("http://www.hltv.org/ranking/teams/")
    teams = page.find("div", {"class": "ranking"})
    teamlist = []
    for team in teams.find_all("div", {"class": "ranked-team standard-box"}):
        newteam = {'name': team.find('div', {"class": "ranking-header"}).select('.name')[0].text.strip(),
                   'rank': converters.to_int(team.select('.position')[0].text.strip(), regexp=True),
                   'rank-points': converters.to_int(team.find('span', {'class': 'points'}).text, regexp=True),
                   'team-id': converters.to_int(team.find('a', {'class': 'details moreLink'})['href'].split('/')[-1]),
                   'team-players': []}
        for player_div in team.find_all("td", {"class": "player-holder"}):
            player = {}
            player['name'] = player_div.find('img', {'class': 'playerPicture'})['title']
            player['player-id'] = converters.to_int(player_div.select('.pointer')[0]['href'].split("/")[-2])
            newteam['team-players'].append(player)
        teamlist.append(newteam)
    return teamlist


def top_players():
    page = get_parsed_page("https://www.hltv.org/stats")
    players = page.find_all("div", {"class": "col"})[0]
    playersArray = []
    for player in players.find_all("div", {"class": "top-x-box standard-box"}):
        playerObj = {}
        playerObj['country'] = player.find_all('img')[1]['alt'].encode('utf8')
        buildName = player.find('img', {'class': 'img'})['alt'].split("'")
        playerObj['name'] = buildName[0].rstrip() + buildName[2]
        playerObj['nickname'] = player.find('a', {'class': 'name'}).text.encode('utf8')
        playerObj['rating'] = player.find('div', {'class': 'rating'}).find('span', {'class': 'bold'}).text.encode('utf8')
        playerObj['maps-played'] = player.find('div', {'class': 'average gtSmartphone-only'}).find('span', {'class': 'bold'}).text.encode('utf8')

        playersArray.append(playerObj)
    return playersArray


def get_players(teamid):
    page = get_parsed_page("http://www.hltv.org/?pageid=362&teamid=" + str(teamid))
    titlebox = page.find("div", {"class": "bodyshot-team"})
    players = []
    for player_link in titlebox.find_all("a"):
        players.append({
            'id': player_link["href"].split("/")[2],
            'nickname': player_link["title"],
            'name': player_link.find("img")['title']
        })

    return players

def get_player_info(player_id):
    """
    :param player_id: integer (or string consisting of integers)
    :return: dictionary of player
    example player id: 7398 (dupreeh)
    """

    page = get_parsed_page(f"https://www.hltv.org/stats/players/{player_id}/a")
    statistics = page.find("div", {"class": "statistics"}).find_all("div", {"class": "stats-row"})
    player_info = {
        'nickname': page.find("h1", {"class": "summaryNickname text-ellipsis"}).text.encode('utf8'),
        'name': page.find("div", {"class": "text-ellipsis"}).text[1:-1].encode('utf8'),
        'country': page.find("img", {"class": "flag"})["alt"],
        'team': page.find("div", {"class": "SummaryTeamname text-ellipsis"}).text.encode('utf8'),
        'age': page.find("div", {"class": "summaryPlayerAge"}).text[:2],
        'stats': {
            'total_kills': statistics[0].find_all("span")[1].text,
            'headshot_percent': statistics[1].find_all("span")[1].text,
            'total_deaths': statistics[2].find_all("span")[1].text,
            'kd_ratio': statistics[3].find_all("span")[1].text,
            'dmg_per_round': statistics[4].find_all("span")[1].text,
            'grenade_dmg_per_round': statistics[5].find_all("span")[1].text,
            'maps_played': statistics[6].find_all("span")[1].text,
            'rounds_played': statistics[7].find_all("span")[1].text,
            'kills_per_round': statistics[8].find_all("span")[1].text,
            'assists_per_round': statistics[9].find_all("span")[1].text,
            'deaths_per_round': statistics[10].find_all("span")[1].text,
            'saved_by_teammate_per_round': statistics[11].find_all("span")[1].text,
            'saved_teammates_per_round': statistics[12].find_all("span")[1].text,
            'rating_1': statistics[13].find_all("span")[1].text,
        }
    }

    return player_info



def get_player_IDS(string):
    playerList = []
    newString = string
    for x in range(5):
        startPointer = newString.find("href=\"/stats/players/")
        stopPointer = newString.find("/", startPointer+21)
        playerID = newString[startPointer + 21:stopPointer]
        newString = newString[stopPointer:]
        startPointer = newString.find("href=\"/stats/players/")
        stopPointer = newString.find("/", startPointer + 21)
        newString = newString[stopPointer:]
        playerList.append(playerID)
    return playerList

def get_player_stats(page):
    words = page.find_all("div", {"class": "stats-section"})
    listOfPlayerIDs = get_player_IDS(str(words))
    ids = {}
    ids[listOfPlayerIDs[0]] = get_player_info(listOfPlayerIDs[0])
    ids[listOfPlayerIDs[1]] = get_player_info(listOfPlayerIDs[1])
    ids[listOfPlayerIDs[2]] = get_player_info(listOfPlayerIDs[2])
    ids[listOfPlayerIDs[3]] = get_player_info(listOfPlayerIDs[3])
    ids[listOfPlayerIDs[4]] = get_player_info(listOfPlayerIDs[4])
    return ids


def get_team_rank(teamID, teamName):
    name = teamName[2:len(teamName)-1]
    page = get_parsed_page("https://www.hltv.org/team/" + teamID + "/" + name)
    html = str(page.find_all("div", {"class": "profile-team-stat"}))
    startPointer = html.find("#")
    stopPointer = html.find("<", startPointer)
    teamRank = html[startPointer+1:stopPointer]
    if len(teamRank) > 10:
        # team is unranked
        rank = 0
    elif int(teamRank) < 11:
        rank = 1
    elif int(teamRank) < 21:
        rank = 2
    elif int(teamRank) < 31:
        rank = 3
    elif int(teamRank) < 41:
        rank = 4
    elif int(teamRank) < 51:
        rank = 5
    elif int(teamRank) < 61:
        rank = 6
    elif int(teamRank) < 71:
        rank = 7
    elif int(teamRank) < 81:
        rank = 8
    elif int(teamRank) < 91:
        rank = 9
    elif int(teamRank) < 101:
        rank = 10
    elif int(teamRank) < 151:
        rank = 11
    elif int(teamRank) < 201:
        rank = 12
    elif int(teamRank) < 251:
        rank = 13
    elif int(teamRank) < 301:
        rank = 14
    else:
        rank = 15
    return rank


def get_team_info(teamid):
    """
    :param teamid: integer (or string consisting of integers)
    :return: dictionary of team
    example team id: 5378 (virtus pro)
    """
    page = get_parsed_page("http://www.hltv.org/?pageid=179&teamid=" + str(teamid))

    team_info = {}
    team_info['team-name'] = page.find("div", {"class": "context-item"}).text.encode('utf8')

    team_info['rank'] = get_team_rank(teamid, str(team_info['team-name']))
    print("grabbed team info, waiting for rate limit")
    time.sleep(5)
    print("done waiting")
    current_lineup = _get_current_lineup(page.find_all("div", {"class": "col teammate"}))
    team_info['current-lineup'] = current_lineup

    #historical_players = _get_historical_lineup(page.find_all("div", {"class": "col teammate"}))
    #team_info['historical-players'] = historical_players

    team_stats_columns = page.find_all("div", {"class": "columns"})
    team_stats = {}

    for columns in team_stats_columns:
        stats = columns.find_all("div", {"class": "col standard-box big-padding"})

        for stat in stats:
            stat_value = stat.find("div", {"class": "large-strong"}).text.encode('utf8')
            stat_title = stat.find("div", {"class": "small-label-below"}).text.encode('utf8')
            team_stats[stat_title] = stat_value

    team_info['stats'] = team_stats

    team_info['playerStats'] = get_player_stats(page)

    return team_info


def get_match_info(match_id):
    """
    Will get match data, NOT map data
    :param match_id: integer (or string consisting of integers)
    :return dictionary of match
    example match id: 65090 (fnatic-vs-nip)
    """
    page = get_parsed_page(f"https://www.hltv.org/stats/matches/{match_id}/a")

    match_info = {
        "team1": {
            "name": page.find_all("table", {"class": "stats-table"})[0].find("th", {"class": "st-teamname"}).text
        },
        "team2": {
            "name": page.find_all("table", {"class": "stats-table"})[1].find("th", {"class": "st-teamname"}).text
        }
    }

    match_info["team1"]["players"] = [player.text for player in page.find_all("table", {"class": "stats-table"})[0].find_all("td", {"class": "st-player"})]
    match_info["team2"]["players"] = [player.text for player in page.find_all("table", {"class": "stats-table"})[1].find_all("td", {"class": "st-player"})]

    for team in ["team1", "team2"]:
        for count, player in enumerate(match_info[team]["players"]):
            stats_table = page.find_all("table", {"class": "stats-table"})[0]
            match_info[team][player] = {
                "kills": stats_table.find_all("td", {"class": "st-kills"})[count].text.split()[0],
                "headshots": stats_table.find_all("td", {"class": "st-kills"})[count].text.split("(")[-1][:-1],
                "assists": stats_table.find_all("td", {"class": "st-assists"})[count].text.split()[0],
                "flash_assists": stats_table.find_all("td", {"class": "st-assists"})[count].text.split("(")[-1][:-1],
                "deaths": stats_table.find_all("td", {"class": "st-deaths"})[count].text,
                "kast": stats_table.find_all("td", {"class": "st-kdratio"})[count].text,
                "kd_diff": stats_table.find_all("td", {"class": "st-kddiff"})[count].text,
                "adr": stats_table.find_all("td", {"class": "st-adr"})[count].text,
                "fk_diff": stats_table.find_all("td", {"class": "st-fkdiff"})[count].text,
                "rating": stats_table.find_all("td", {"class": "st-rating"})[count].text,
            }

    return match_info

def _get_current_lineup(player_anchors):
    """
    helper function for function above
    :return: list of players
    """
    players = []
    for player_anchor in player_anchors[0:5]:
        player = {}
        buildName = player_anchor.find("img", {"class": "container-width"})["alt"].split('\'')
        player['country'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("img", {"class": "flag"})["alt"]
        player['name'] = buildName[0].rstrip() + buildName[2]
        player['nickname'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("div", {"class": "text-ellipsis"}).text
        player['maps-played'] = int(re.search(r'\d+', player_anchor.find("div", {"class": "teammate-info standard-box"}).find("span").text).group())
        players.append(player)
    return players

def _get_historical_lineup(player_anchors):
    """
    helper function for function above
    :return: list of players
    """
    players = []
    for player_anchor in player_anchors[5::]:
        player = {}
        buildName = player_anchor.find("img", {"class": "container-width"})["alt"].split('\'')
        player['country'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("img", {"class": "flag"})["alt"].encode('utf8')
        player['name'] = buildName[0].rstrip() + buildName[2]
        player['nickname'] = player_anchor.find("div", {"class": "teammate-info standard-box"}).find("div", {"class": "text-ellipsis"}).text.encode('utf8')
        player['maps-played'] = int(re.search(r'\d+', player_anchor.find("div", {"class": "teammate-info standard-box"}).find("span").text).group())
        players.append(player)
    return players


def get_matches():
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matches_list = []
    upcomingmatches = matches.find("div", {"class": "upcomingMatchesSection"})

    matchdays = matches.find_all("div", {"class": "upcomingMatchesSection"})

    for match in matchdays:
        matchDetails = match.find_all("div", {"class": "upcomingMatch"})
        date = match.find({'span': {'class': 'matchDayHeadline'}}).text.split()[-1]
        for getMatch in matchDetails:
            matchObj = {}

            matchObj['date'] = date
            matchObj['time'] = getMatch.find("div", {"class": "matchTime"}).text
            if getMatch.find("div", {"class": "matchEvent"}):
                matchObj['event'] = getMatch.find("div", {"class": "matchEvent"}).text.encode('utf8').strip()
            else:
                matchObj['event'] = getMatch.find("div", {"class": "matchInfoEmpty"}).text.encode('utf8').strip()

            if (getMatch.find_all("div", {"class": "matchTeams"})):
                matchObj['team1'] = getMatch.find_all("div", {"class": "matchTeam"})[0].text.encode('utf8').lstrip().rstrip()
                matchObj['team2'] = getMatch.find_all("div", {"class": "matchTeam"})[1].text.encode('utf8').lstrip().rstrip()
            else:
                matchObj['team1'] = None
                matchObj['team2'] = None

            matches_list.append(matchObj)

    return matches_list


def get_current_date():
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    return d


def get_team_ID(string, team):
    if team == 'team1':
        starter = string.find("team1=")
        stopper = string.find("\"", starter+7)
        result = string[starter+7:stopper]
        return result
    else:
        starter = string.find("team2=")
        stopper = string.find("\"", starter + 7)
        result = string[starter + 7:stopper]
        return result


def get_todays_matches():
    matches = get_parsed_page("http://www.hltv.org/matches/")
    matches_list = []
    upcomingmatches = matches.find("div", {"class": "upcomingMatchesSection"})

    matchdays = matches.find_all("div", {"class": "upcomingMatchesSection"})

    for match in matchdays:
        matchDetails = match.find_all("div", {"class": "upcomingMatch"})
        date = match.find({'span': {'class': 'matchDayHeadline'}}).text.split()[-1]
        for getMatch in matchDetails:
            matchObj = {}

            matchObj['date'] = date
            matchObj['time'] = getMatch.find("div", {"class": "matchTime"}).text
            if getMatch.find("div", {"class": "matchEvent"}):
                matchObj['event'] = getMatch.find("div", {"class": "matchEvent"}).text.encode('utf8').strip()
            else:
                matchObj['event'] = getMatch.find("div", {"class": "matchInfoEmpty"}).text.encode('utf8').strip()

            if (getMatch.find_all("div", {"class": "matchTeams"})):
                matchObj['team1'] = getMatch.find_all("div", {"class": "matchTeam"})[0].text.encode('utf8').lstrip().rstrip()
                matchObj['team1ID'] = get_team_ID(str(getMatch), 'team1')
                matchObj['team2'] = getMatch.find_all("div", {"class": "matchTeam"})[1].text.encode('utf8').lstrip().rstrip()
                matchObj['team2ID'] = get_team_ID(str(getMatch), 'team2')
            else:
                matchObj['team1'] = None
                matchObj['team2'] = None
            if(date == get_current_date()):
                matches_list.append(matchObj)

    return matches_list

def get_results():
    results = get_parsed_page("http://www.hltv.org/results/")

    results_list = []

    pastresults = results.find_all("div", {"class": "results-holder"})

    for result in pastresults:
        resultDiv = result.find_all("div", {"class": "result-con"})

        for res in resultDiv:
            getRes = res.find("div", {"class": "result"}).find("table")

            resultObj = {}

            if (res.parent.find("span", {"class": "standard-headline"})):
                resultObj['date'] = res.parent.find("span", {"class": "standard-headline"}).text.encode('utf8')
            else:
                dt = datetime.date.today()
                resultObj['date'] = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)

            if (res.find("td", {"class": "placeholder-text-cell"})):
                resultObj['event'] = res.find("td", {"class": "placeholder-text-cell"}).text.encode('utf8')
            elif (res.find("td", {"class": "event"})):
                resultObj['event'] = res.find("td", {"class": "event"}).text.encode('utf8')
            else:
                resultObj['event'] = None

            if (res.find_all("td", {"class": "team-cell"})):
                resultObj['team1'] = res.find_all("td", {"class": "team-cell"})[0].text.encode('utf8').lstrip().rstrip()
                resultObj['team1score'] = converters.to_int(res.find("td", {"class": "result-score"}).find_all("span")[0].text.encode('utf8').lstrip().rstrip())
                resultObj['team2'] = res.find_all("td", {"class": "team-cell"})[1].text.encode('utf8').lstrip().rstrip()
                resultObj['team2score'] = converters.to_int(res.find("td", {"class": "result-score"}).find_all("span")[1].text.encode('utf8').lstrip().rstrip())
            else:
                resultObj['team1'] = None
                resultObj['team2'] = None

            results_list.append(resultObj)

    return results_list


def get_todays_results():
    results = get_parsed_page("http://www.hltv.org/results/")

    results_list = []

    pastresults = results.find_all("div", {"class": "results-holder"})
    pastresults = pastresults[1:]

    for result in pastresults:
        resultDiv = result.find_all("div", {"class": "result-con"})

        for res in resultDiv:
            getRes = res.find("div", {"class": "result"}).find("table")

            resultObj = {}

            day = res.parent.find("span", {"class": "standard-headline"}).text.encode('utf8')
            date = day.decode()
            date = date[12:]
            format = 'MMMM Do YYYY'
            date = arrow.get(date, format).format('YYYY-MM-DD')
            resultObj['date'] = date

            if (res.find("td", {"class": "placeholder-text-cell"})):
                resultObj['event'] = res.find("td", {"class": "placeholder-text-cell"}).text.encode('utf8')
            elif (res.find("td", {"class": "event"})):
                resultObj['event'] = res.find("td", {"class": "event"}).text.encode('utf8')
            else:
                resultObj['event'] = None

            if (res.find_all("td", {"class": "team-cell"})):
                resultObj['team1'] = res.find_all("td", {"class": "team-cell"})[0].text.encode('utf8').lstrip().rstrip()
                resultObj['team1score'] = converters.to_int(
                    res.find("td", {"class": "result-score"}).find_all("span")[0].text.encode('utf8').lstrip().rstrip())
                resultObj['team2'] = res.find_all("td", {"class": "team-cell"})[1].text.encode('utf8').lstrip().rstrip()
                resultObj['team2score'] = converters.to_int(
                    res.find("td", {"class": "result-score"}).find_all("span")[1].text.encode('utf8').lstrip().rstrip())
            else:
                resultObj['team1'] = None
                resultObj['team2'] = None

            if date == get_current_date():
                results_list.append(resultObj)

    return results_list

def get_results_by_date(start_date, end_date):
    # Dates like yyyy-mm-dd  (iso)
    results_list = []
    offset = 0
    # Loop through all stats pages
    while True:
        url = "https://www.hltv.org/stats/matches?startDate="+start_date+"&endDate="+end_date+"&offset="+str(offset)

        results = get_parsed_page(url)

        # Total amount of results of the query
        amount = int(results.find("span", attrs={"class": "pagination-data"}).text.split("of")[1].strip())

        # All rows (<tr>s) of the match table
        pastresults = results.find("tbody").find_all("tr")

        # Parse each <tr> element to a result dictionary
        for result in pastresults:
            team_cols = result.find_all("td", {"class": "team-col"})
            t1 = team_cols[0].find("a").text
            t2 = team_cols[1].find("a").text
            t1_score = int(team_cols[0].find_all(attrs={"class": "score"})[0].text.strip()[1:-1])
            t2_score = int(team_cols[1].find_all(attrs={"class": "score"})[0].text.strip()[1:-1])
            map = result.find(attrs={"class": "statsDetail"}).find(attrs={"class": "dynamic-map-name-full"}).text
            event = result.find(attrs={"class": "event-col"}).text
            date = result.find(attrs={"class": "date-col"}).find("a").find("div").text

            result_dict = {"team1": t1, "team2": t2, "team1score": t1_score,
                           "team2score": t2_score, "date": date, "map": map, "event": event}

            # Add this pages results to the result list
            results_list.append(result_dict)

        # Get the next 50 results (next page) or break
        if offset < amount:
            offset += 50
        else:
            break

    return results_list

