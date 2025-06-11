from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
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

# Finding the links for each player.
qb_links = table_qb.find_all('a')
rb_links = table_rb.find_all('a')
wr_links = table_wr.find_all('a')
te_links = table_te.find_all('a')
k_links = table_k.find_all('a')

# Iterates through all the <a> tags, and finds the href link. We are also making sure that there are no links passed through that are
# different than what we are looking for.
qb_links = [l.get("href") for l in qb_links]
rb_links = [l.get("href") for l in rb_links]
wr_links = [l.get("href") for l in wr_links]
te_links = [l.get("href") for l in te_links]
k_links = [l.get("href") for l in k_links]

qb_links = [l for l in qb_links if 'nfl/stats' in l]
rb_links = [l for l in rb_links if 'nfl/stats' in l]
wr_links = [l for l in wr_links if 'nfl/stats' in l]
te_links = [l for l in te_links if 'nfl/stats' in l]
k_links = [l for l in k_links if 'nfl/stats' in l]

# Getting the individual player links
qb_urls = [f"https://fantasypros.com{l}" for l in qb_links]
rb_urls = [f"https://fantasypros.com{l}" for l in rb_links]
wr_urls = [f"https://fantasypros.com{l}" for l in wr_links]
te_urls = [f"https://fantasypros.com{l}" for l in te_links]
k_urls = [f"https://fantasypros.com{l}" for l in k_links]

# Extracting data for defensive special teams.
dst_teams = soup_dst.find_all(class_ = re.compile("mpb-player-"))
player_data = pd.read_html(StringIO(str(table_dst)))[0]
player_data = player_data.drop(player_data.columns[0], axis=1)
print(player_data)
all_players.append(player_data)

# We are now sorting through every individual qb link, and each page has the same format, so we can take data from them the same way.
for qb_url in qb_urls:
    html = requests.get(qb_url).text
    soup = BeautifulSoup(html, "lxml")
    player_name = soup.find("h1", class_ = re.compile("player-")).text
    player_position = "QB"
    bio_details = soup.find_all(class_ = "bio-detail")
    player_height = bio_details[0].text if len(bio_details) > 0 else "N/A"
    player_weight = bio_details[1].text if len(bio_details) > 1 else "N/A"
    player_age = bio_details[2].text if len(bio_details) > 2 else "N/A"
    
    print(player_height)
    
    # This finds the table with the passing stats for QBs.
    all_stats = soup.find_all('table', class_ = re.compile("table table-bordered"))
    
    for stats in all_stats:
        if stats and stats.columns:
            # Formatting the stats
            stats.columns = stats.columns.droplevel()
        
        player_data = pd.read_html(StringIO(str(stats)))[0]
        player_data["Player"] = player_name
        player_data["Position"] = player_position
        player_data["Height"] = player_height
        player_data["Weight"] = player_weight
        player_data["Age"] = player_age
        
        print(player_data)
        
        all_players.append(player_data)
        time.sleep(5)
        
for rb_url in rb_urls:
    html = requests.get(rb_url).text
    soup = BeautifulSoup(html, "lxml")
    player_name = soup.find("h1", class_ = re.compile("player-")).text
    player_position = "RB"
    bio_details = soup.find_all(class_ = "bio-detail")
    player_height = bio_details[0].text if len(bio_details) > 0 else "N/A"
    player_weight = bio_details[1].text if len(bio_details) > 1 else "N/A"
    player_age = bio_details[2].text if len(bio_details) > 2 else "N/A"
    
    # This finds the table with the passing stats for QBs.
    all_stats = soup.find_all('table', class_ = re.compile("table table-bordered"))
    
    for stats in all_stats:
        if stats and stats.columns:
            # Formatting the stats
            stats.columns = stats.columns.droplevel()
        
        player_data = pd.read_html(StringIO(str(stats)))[0]
        player_data["Player"] = player_name
        player_data["Position"] = player_position
        player_data["Height"] = player_height
        player_data["Weight"] = player_weight
        player_data["Age"] = player_age
        print(player_data)
        
        all_players.append(player_data)
        time.sleep(5)


for wr_url in wr_urls:
    html = requests.get(wr_url).text
    soup = BeautifulSoup(html, "lxml")
    player_name = soup.find("h1", class_ = re.compile("player-")).text
    player_position = "WR"
    bio_details = soup.find_all(class_ = "bio-detail")
    player_height = bio_details[0].text if len(bio_details) > 0 else "N/A"
    player_weight = bio_details[1].text if len(bio_details) > 1 else "N/A"
    player_age = bio_details[2].text if len(bio_details) > 2 else "N/A"
     
    
    # This finds the table with the passing stats for QBs.
    all_stats = soup.find_all('table', class_ = re.compile("table table-bordered"))
    
    for stats in all_stats:
        if stats and stats.columns:
            # Formatting the stats
            stats.columns = stats.columns.droplevel()
        
        player_data = pd.read_html(StringIO(str(stats)))[0]
        player_data["Player"] = player_name
        player_data["Position"] = player_position
        player_data["Height"] = player_height
        player_data["Weight"] = player_weight
        player_data["Age"] = player_age
        print(player_data)
        
        all_players.append(player_data)
        time.sleep(5)
        

for te_url in te_urls:
    html = requests.get(te_url).text
    soup = BeautifulSoup(html, "lxml")
    player_name = soup.find("h1", class_ = re.compile("player-")).text
    player_position = "TE"
    bio_details = soup.find_all(class_ = "bio-detail")
    player_height = bio_details[0].text if len(bio_details) > 0 else "N/A"
    player_weight = bio_details[1].text if len(bio_details) > 1 else "N/A"
    player_age = bio_details[2].text if len(bio_details) > 2 else "N/A"
    
    # This finds the table with the passing stats for QBs.
    all_stats = soup.find_all('table', class_ = re.compile("table table-bordered"))
    
    for stats in all_stats:
        if stats and stats.columns:
            # Formatting the stats
            stats.columns = stats.columns.droplevel()
        
        player_data = pd.read_html(StringIO(str(stats)))[0]
        player_data["Player"] = player_name
        player_data["Position"] = player_position
        player_data["Height"] = player_height
        player_data["Weight"] = player_weight
        player_data["Age"] = player_age
        print(player_data)
        
        all_players.append(player_data)
        time.sleep(5)
        

for k_url in k_urls:
    html = requests.get(k_url).text
    soup = BeautifulSoup(html, "lxml")
    player_name = soup.find("h1", class_ = re.compile("player-")).text
    player_position = "K"
    bio_details = soup.find_all(class_ = "bio-detail")
    player_height = bio_details[0].text if len(bio_details) > 0 else "N/A"
    player_weight = bio_details[1].text if len(bio_details) > 1 else "N/A"
    player_age = bio_details[2].text if len(bio_details) > 2 else "N/A"
    
    # This finds the table with the passing stats for QBs.
    all_stats = soup.find_all('table', class_ = re.compile("table table-bordered"))
    
    for stats in all_stats:
        if stats and stats.columns:
            # Formatting the stats
            stats.columns = stats.columns.droplevel()
        
        player_data = pd.read_html(StringIO(str(stats)))[0]
        player_data["Player"] = player_name
        player_data["Position"] = player_position
        player_data["Height"] = player_height
        player_data["Weight"] = player_weight
        player_data["Age"] = player_age
        print(player_data)
        
        all_players.append(player_data)
        time.sleep(5)

stat_df = pd.concat(all_players)
stat_df.to_csv("All_Player_Stats.csv")
