import httplib2
from bs4 import BeautifulSoup
import requests
import random
from requests_html import HTMLSession

user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

]

#/html/body/div[2]/div[2]/section/section[2]/section/div[2]/div/section/div[4]/div/div/div[2]/div/div
def get_player_point_overunder(link):
    overunders = {}
    custom_headers = {
            'user-agent':  random.choice(user_agent_list),
            'Accept-Language': 'en-US,en;q=0.9'
    }
    session = HTMLSession()
    response = session.get(link)
    response.html.render()
    games = response.html.find("tbody.sportsbook-table__body")
    for game in games:
        for playeroptions in game.find('tr'):
            playername = playeroptions.find('th',first=True).find('div',first=True).find('a',first=True).find('span',first=True).text
            points = playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div',first=True).find('div',first=True).find('span')[2].text
            over =  playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text
            under =  playeroptions.find('td')[1].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text
            overunders[playername] = (points, over, under)

    print(overunders)

    return

get_player_point_overunder('https://sportsbook.draftkings.com/leagues/basketball/nba?category=player-points&subcategory=points-o%2Fu')
