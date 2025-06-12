from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from io import StringIO
import datetime

# Empty arrays for all of the players that matter for a fantasy football platform.
all_players = []

today = datetime.date.today()
nfl_week_1 = datetime.date(2025, 9, 5)  # Update later if needed

if today < nfl_week_1:
    html_qb = requests.get("https://www.fantasypros.com/nfl/projections/qb.php").text
    html_rb = requests.get("https://www.fantasypros.com/nfl/projections/rb.php").text
    html_wr = requests.get("https://www.fantasypros.com/nfl/projections/wr.php").text
    html_te = requests.get("https://www.fantasypros.com/nfl/projections/te.php").text
    html_k = requests.get("https://www.fantasypros.com/nfl/projections/k.php").text
    html_dst = requests.get("https://www.fantasypros.com/nfl/projections/dst.php").text
else:
    html_qb = requests.get("https://www.fantasypros.com/nfl/stats/qb.php").text
    html_rb = requests.get("https://www.fantasypros.com/nfl/stats/rb.php").text
    html_wr = requests.get("https://www.fantasypros.com/nfl/stats/wr.php").text
    html_te = requests.get("https://www.fantasypros.com/nfl/stats/te.php").text
    html_k = requests.get("https://www.fantasypros.com/nfl/stats/k.php").text
    html_dst = requests.get("https://www.fantasypros.com/nfl/stats/dst.php").text
    
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


# qb_names = soup_qb.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_qb)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "QB"
# all_players.append(player_data)

# rb_names = soup_rb.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_rb)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "RB"
# all_players.append(player_data)

# wr_names = soup_wr.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_wr)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "WR"
# all_players.append(player_data)

# te_names = soup_qb.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_te)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "TE"
# all_players.append(player_data)

# k_names = soup_k.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_k)))[0]
# #player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "K"
# all_players.append(player_data)

# dst_teams = soup_dst.find_all(class_ = re.compile("mpb-player-"))
# player_data = pd.read_html(StringIO(str(table_dst)))[0]
# #player_data = player_data.drop(player_data.columns[0], axis=1)
# player_data["Position"] = "DST"
# all_players.append(player_data)

qb_names = soup_qb.find_all(class_=re.compile("mpb-player-"))
qb_ids = []
for el in qb_names:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            qb_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_qb)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = qb_ids
player_data["Position"] = "QB"
all_players.append(player_data)


rb_names = soup_rb.find_all(class_=re.compile("mpb-player-"))
rb_ids = []
for el in rb_names:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            rb_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_rb)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = rb_ids
player_data["Position"] = "RB"
all_players.append(player_data)


wr_names = soup_wr.find_all(class_=re.compile("mpb-player-"))
wr_ids = []
for el in wr_names:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            wr_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_wr)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = wr_ids
player_data["Position"] = "WR"
all_players.append(player_data)


te_names = soup_te.find_all(class_=re.compile("mpb-player-"))
te_ids = []
for el in te_names:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            te_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_te)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = te_ids
player_data["Position"] = "TE"
all_players.append(player_data)


k_names = soup_k.find_all(class_=re.compile("mpb-player-"))
k_ids = []
for el in k_names:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            k_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_k)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = k_ids
player_data["Position"] = "K"
all_players.append(player_data)


dst_teams = soup_dst.find_all(class_=re.compile("mpb-player-"))
dst_ids = []
for el in dst_teams:
    classes = el.get("class", [])
    for c in classes:
        if c.startswith("mpb-player-"):
            dst_ids.append(c.replace("mpb-player-", ""))
            break
player_data = pd.read_html(StringIO(str(table_dst)))[0]
# player_data = player_data.drop(player_data.columns[0], axis=1)
player_data["externalId"] = dst_ids
player_data["Position"] = "DST"
all_players.append(player_data)

stat_df = pd.concat(all_players)

# Fix multi-level column headers if they exist:
if isinstance(stat_df.columns, pd.MultiIndex):
    stat_df.columns = stat_df.columns.get_level_values(-1)

from collections import Counter

duplicates = [item for item, count in Counter(stat_df.columns).items() if count > 1]
print("Duplicate columns before conv cols to strings:", duplicates)

# Convert all columns to strings:
stat_df.columns = [ 
    ' '.join(col).strip() if isinstance(col, tuple) else str(col)
    for col in stat_df.columns
]

from collections import Counter

seen = Counter()
new_columns = []

for col in stat_df.columns:
    new_name = col
    if re.search(r"Player", col, re.IGNORECASE):
        new_name = "fullName"
    elif re.search(r"Position", col, re.IGNORECASE):
        new_name = "position"
    elif re.search(r"externalId", col, re.IGNORECASE):
        new_name = "id"

    seen[new_name] += 1
    if seen[new_name] > 1:
        new_name += f"_{seen[new_name] - 1}"

    new_columns.append(new_name)

stat_df.columns = new_columns

stat_df.columns = new_columns

from collections import Counter

duplicates = [item for item, count in Counter(stat_df.columns).items() if count > 1]
print("Duplicate columns after conv cols to strings and new col updates:", duplicates)

stat_df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in stat_df.columns]
    
stat_df.to_csv("Players.csv", index=False)

df = pd.read_csv("Players.csv")
