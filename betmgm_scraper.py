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



user_agent_list = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 

}

#/html/body/div[2]/div[2]/section/section[2]/section/div[2]/div/section/div[4]/div/div/div[2]/div/div
def get_player_point_overunder(link):
    overunders = {}
    driver = webdriver.Chrome(options=op)
    driver.get(link)
    time.sleep(3)
    driver.find_element(By.XPATH, './/*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-option-panel-bottom-action/div').click()
    table = driver.find_element(By.XPATH, '//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-split-header/div')
    content = table.find_elements(By.XPATH, "./*")
    
    for i in range(1, len(content), 3):
        playername = content[i].find_element(By.CLASS_NAME, "player-props-player-name").text
        points = content[i+1].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "name").text[5:]
        over = content[i+1].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        under = content[i+2].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        overunders[playername] = (points, over, under)


    return
    # return

get_player_point_overunder('https://sports.mi.betmgm.com/en/sports/events/boston-celtics-at-washington-wizards-16243435?market=Players:Points&tab=score')
