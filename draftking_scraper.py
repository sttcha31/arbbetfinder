import csv
import multiprocessing
from requests_html import HTMLSession

def get_player_overunder(category):
    link = "https://sportsbook.draftkings.com/leagues/basketball/nba?category=player-"+category+"&subcategory="+category+"-o%2Fu"
    overunders = []
    session = HTMLSession()
    response = session.get(link)
    response.html.render()
    games = response.html.find("tbody.sportsbook-table__body")
    for game in games:
        for playeroptions in game.find('tr'):
            overunder = {}
            overunder["sportsbook"] = "DraftKing"
            overunder["player_name"]= playeroptions.find('th',first=True).find('div',first=True).find('a',first=True).find('span',first=True).text
            overunder["category"] = category
            overunder["value"]= playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div',first=True).find('div',first=True).find('span')[2].text
            overunder["over"] =  playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text
            overunder["under"] =  playeroptions.find('td')[1].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text
            overunders.append(overunder)
    write_to_csv(overunders)
    print(overunders)

    return

def write_to_csv(data):
    with open("odds.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)

if __name__ == '__main__':
    tasks = list()
    tasks.append("points")
    tasks.append("assists")
    tasks.append("rebounds")
    tasks.append("threes")
    with multiprocessing.Pool(processes=len(tasks)) as pool:
        results = pool.map(get_player_overunder, tasks)