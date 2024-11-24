import httplib2
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
from requests_html import HTMLSession
import time
op = webdriver.ChromeOptions()
# op.add_argument('headless')
op.add_argument("--enable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
op.add_argument("--enable-javascript")

def get_game_links():
    driver = webdriver.Chrome(options=op)
    driver.get("https://sports.mi.betmgm.com/en/sports/basketball-7/betting/usa-9/nba-6004")
    wait = WebDriverWait(driver, 20)
    #CHECK: following line's XPATH might chance from day to day
                                                                
    table = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ms-widget-layout/ms-widget-slot/ms-composable-widget/ms-widget-slot/ms-tabbed-grid-widget/ms-grid/div/ms-event-group')))
    games = table.find_elements(By.XPATH, "./*")
    with open("mgmgames.txt", "w") as file: 
        for game in games:
            file.write(game.find_element(By.CLASS_NAME, "grid-event-wrapper").find_element(By.TAG_NAME, "a").get_attribute("href") + "\n")

def get_player_overunder(link, category):
    overunders = {}
    driver = webdriver.Chrome(options=op)
    driver.get(link+"?market=Players:"+category)
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-option-panel-bottom-action/div')))
    button.click()

    table = driver.find_element(By.XPATH, '//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-split-header/div')
    print(table)

    content = table.find_elements(By.XPATH, "./*")
    for i in range(1, len(content)):
        playername = content[i].find_element(By.CLASS_NAME, "player-props-player-name").text
        points = content[i].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "name").text[2:]
        over = content[i].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        under = content[i].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        overunders[playername] = (points, over, under)

    print(overunders)
    return overunders

def write_to_csv(overunders):
    return


# get_player_overunder('https://sports.mi.betmgm.com/en/sports/events/minnesota-timberwolves-at-boston-celtics-16529704', "Points")
# get_player_overunder('https://sports.mi.betmgm.com/en/sports/events/brooklyn-nets-at-orlando-magic-16517249?tab=score&market=Players', "Rebounds")
# get_player_overunder('https://sports.mi.betmgm.com/en/sports/events/brooklyn-nets-at-orlando-magic-16517249?tab=score&market=Players', "Assists")
# get_player_overunder('https://sports.mi.betmgm.com/en/sports/events/brooklyn-nets-at-orlando-magic-16517249?tab=score&market=Players', "3-Pointers")

# get_game_links()


