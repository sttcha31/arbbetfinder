import csv
from requests_html import AsyncHTMLSession
import asyncio
from requests_html import HTMLSession

async def get_player_overunder(category):
    link = "https://sportsbook.draftkings.com/leagues/basketball/nba?category=player-"+category+"&subcategory="+category+"-o%2Fu"
    overunders = []
    # session = HTMLSession()
    # response = session.get(link)
    # response.html.render()
    session = AsyncHTMLSession()
    response = await session.get(link)
    await response.html.arender(sleep=2)    
    games = response.html.find("tbody.sportsbook-table__body")
    for game in games:
        for playeroptions in game.find('tr'):
            overunder = {}
            overunder["sportsbook"] = "DraftKing"
            overunder["player_name"]= playeroptions.find('th',first=True).find('div',first=True).find('a',first=True).find('span',first=True).text
            if(category =='points'):
                overunder["category"] = "Points"
            if(category =='assists'):
                overunder["category"] = "Assists"
            if(category =='rebounds'):
                overunder["category"] = "Rebound"
            if(category =='threes'):
                overunder["category"] = "ThreePointer"
    
            overunder["value"]= playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div',first=True).find('div',first=True).find('span')[2].text
            if (over:=playeroptions.find('td')[0].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text)[0] != "+":
                over = "-" + over[1:]
            overunder["over"] =  over
            if (under:=playeroptions.find('td')[1].find('div',first=True).find('div',first=True).find('div.sportsbook-outcome-body-wrapper', first="0").find("div")[2].find("div")[2].find("span", first=True).text)[0] != "+":
                under = "-" + under[1:]
            overunder["under"] = under
            overunders.append(overunder)
    write_to_csv(overunders)
    print(overunders)

    return

def write_to_csv(data):
    with open("odds.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)


async def main():
    tasks = ["points", "assists", "rebounds", "threes"]
    await asyncio.gather(*(get_player_overunder(category) for category in tasks))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        # Suppress "Event loop is closed" errors during Pyppeteer cleanup
        if "Event loop is closed" not in str(e):
            raise