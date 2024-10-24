import httplib2
from bs4 import BeautifulSoup
import requests
import random
from requests_html import HTMLSession

def get_player_point_overunder(link):
    overunders = {}
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
