from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from io import StringIO

# Empty arrays for all of the players that matter for a fantasy football platform.
all_players = []

# Getting the url that has the players for each position (a different url for each position).
html_qb = requests.get("https://www.fantasypros.com/nfl/stats/qb.php").text
html_rb = requests.get("https://www.fantasypros.com/nfl/stats/rb.php").text
html_wr = requests.get("https://www.fantasypros.com/nfl/stats/wr.php").text
html_te = requests.get("https://www.fantasypros.com/nfl/stats/te.php").text
html_k = requests.get("https://www.fantasypros.com/nfl/stats/k.php").text
html_dst = requests.get("https://www.fantasypros.com/nfl/stats/dst.php").text

# Using BeautifulSoup to make parsing the html easy.
soup_qb = BeautifulSoup(html_qb, "lxml")
soup_rb = BeautifulSoup(html_rb, "lxml")
soup_wr = BeautifulSoup(html_wr, "lxml")
soup_te = BeautifulSoup(html_te, "lxml")
soup_k = BeautifulSoup(html_k, "lxml")
soup_dst = BeautifulSoup(html_dst, "lxml")

# Finding the tables we care about.
table_qb = soup_qb.find_all(id="data")[0]
table_rb = soup_rb.find_all(id="data")[0]
table_wr = soup_wr.find_all(id="data")[0]
table_te = soup_te.find_all(id="data")[0]
table_k = soup_k.find_all(id="data")[0]
table_dst = soup_dst.find_all(id="data")[0]


qb_names = soup_qb.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_qb)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "QB"
all_players.append(player_data)

rb_names = soup_rb.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_rb)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "RB"
all_players.append(player_data)

wr_names = soup_wr.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_wr)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "WR"
all_players.append(player_data)

te_names = soup_qb.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_te)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "TE"
all_players.append(player_data)

k_names = soup_k.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_k)))[0]
#player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "K"
all_players.append(player_data)

dst_teams = soup_dst.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_dst)))[0]
#player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["Position"] = "DST"
all_players.append(player_data)

stat_df = pd.concat(all_players)
stat_df.to_csv("Players.csv")
print(all_players)
