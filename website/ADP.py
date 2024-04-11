from bs4 import BeautifulSoup, Tag
import requests

def scrape_players_data():
   url ='https://www.fantasypros.com/nfl/adp/ppr-overall.php'

   page = requests.get(url)

   soup = BeautifulSoup(page.text, 'html.parser')
   tbody = soup.tbody
   trs = tbody.contents

   # print(trs[2])

   players = {}

   # for tr in trs:
   #     if isinstance(tr, Tag):
   #         name, adp = tr.contents[2:5]
   #         print(adp)
         
   for index, tr in enumerate(trs):
      if index >= 250:
         break

      if isinstance(tr, Tag):  # Check if the object is a Tag
            name = tr.contents[2].a.string
            team_tag = tr.find(class_='player-label').find('small')
            team = team_tag.get_text(strip=True) if team_tag else ""
            # player_info = tr.contents[2].find_all('small')  # Find all <small> tags within the second <td> tag
            # if len(player_info) >= 2:  # Check if there are at least two <small> tags
            #    team = player_info[0].get_text(strip=True)
            #    # byeWeek = player_info[1].get_text(strip=True)
            # else:
            #    team = ""
               # bye_week = ""
            positionRank = tr.contents[4].get_text(strip=True)
            sleeperADP_text = tr.contents[5].get_text(strip=True)
            if sleeperADP_text:
               sleeperADP = float(sleeperADP_text)
            else:
               sleeperADP = 1000.0
         #  print("Name:", name.a.string)
         #  print("Team:", team)
         #  print("Bye Week:", byeWeek)
         #  print("Position Rank:", positionRank.string)
         #  print("Sleeper ADP:", sleeperADP.string)
         #  print()
            
            players[name] = {
               'Name': name,
               'Team': team,
               # 'Bye Week': byeWeek,
               'Position Rank': positionRank,
               'Sleeper ADP': sleeperADP
         }
   
   sorted_players = sorted(players.values(), key=lambda x: x['Sleeper ADP'])


   return sorted_players

   # for player_name, player_data in players.items():
   #     print("Name:", player_name)
   #     for key, value in player_data.items():
   #         print(key + ":", value)
   #     print()



# url ='https://www.fantasypros.com/nfl/adp/ppr-overall.php'

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html.parser')
# tbody = soup.tbody
# trs = tbody.contents

# # print(trs[2])

# players = {}

# # for tr in trs:
# #     if isinstance(tr, Tag):
# #         name, adp = tr.contents[2:5]
# #         print(adp)
      
# for index, tr in enumerate(trs):
#    if index >= 250:
#       break

#    if isinstance(tr, Tag):  # Check if the object is a Tag
#          name = tr.contents[2].get_text(strip=True)
#          player_info = tr.contents[2].find_all('small')  # Find all <small> tags within the second <td> tag
#          if len(player_info) >= 2:  # Check if there are at least two <small> tags
#             team = player_info[0].get_text(strip=True)
#             byeWeek = player_info[1].get_text(strip=True)
#          else:
#             team = ""
#             bye_week = ""
#          positionRank = tr.contents[4].get_text(strip=True)
#          sleeperADP_text = tr.contents[7].get_text(strip=True)
#          if sleeperADP_text:
#             sleeperADP = float(sleeperADP_text)
#          else:
#             sleeperADP = 1000.0
         
#       #  print("Name:", name.a.string)
#       #  print("Team:", team)
#       #  print("Bye Week:", byeWeek)
#       #  print("Position Rank:", positionRank.string)
#       #  print("Sleeper ADP:", sleeperADP.string)
#       #  print()
         
#          players[name] = {
#             'Team': team,
#             'Bye Week': byeWeek,
#             'Position Rank': positionRank,
#             'Sleeper ADP': sleeperADP
#       }

# sorted_players = sorted(players.values(), key=lambda x: x['Sleeper ADP'])

# print(sorted_players)