import multiprocessing
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
op = webdriver.ChromeOptions()

op.add_argument("--enable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
op.add_argument("--enable-javascript")
def get_player_overunder(category):
    if (category == "Points"): link = "https://espnbet.com/sport/basketball/organization/united-states/competition/nba/event/0cd158b9-eac5-4644-b1c3-f9f2eaa2d90a/section/player_props"
    driver = webdriver.Chrome(options=op)
    driver.get(link)
    time.sleep(10)
    wait = WebDriverWait(driver, 20)

    # session = AsyncHTMLSession()
    # response = await session.get(link)
    # await response.html.arender(sleep=2)  
    # print(response.html)  
    # gamesname = response.html.find(
    #     'div',
    # )
    # print(gamesname)
    # for game in gamesname:
    #     for playeroptions in game.find('div')[1:]:
    #         print("here")
    #         names.append(playeroptions.find('div.srb-ParticipantLabelWithTeam_Name').text)
    # print(names)

    return

def write_to_csv(data):
    with open("odds.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)


# async def main():
#     tasks = ["points", "assists", "rebounds", "threes"]
#     await asyncio.gather(*(get_player_overunder(category) for category in tasks))

# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except RuntimeError as e:
#         # Suppress "Event loop is closed" errors during Pyppeteer cleanup
#         if "Event loop is closed" not in str(e):
#             raise

get_player_overunder("Points")