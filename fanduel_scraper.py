import httplib2
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
from requests_html import HTMLSession
import time
op = webdriver.ChromeOptions()
# op.add_argument('headless')
op.add_argument("--enable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
op.add_argument("--enable-javascript")



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
    driver = webdriver.Chrome(options=op)
    driver.get(link)
    time.sleep(10)
    # print("here")
    # clicknhold = driver.find_element(By.XPATH, './/p[text()="Press & Hold"]')
    # print("here")
    # humanverif = ActionChains(driver)
    # humanverif.click_and_hold(clicknhold).perform()
    # time.sleep(10)
    
    # humanverif.relase(clicknhold).perform()
    # time.sleep(2)
    driver.find_element(By.CLASS_NAME, "v w al y by ci t is h il").click()
    time.sleep(10)
    # options = driver.find_elements(By.CSS_SELECTOR, ".v.w.x.y.bv.cf.t.es.h")
    # print(options)
    # for playeroptions in options:
    #     print(playeroptions)
    # return

get_player_point_overunder('https://sportsbook.fanduel.com/navigation/nba')

# sypNMOnZZzLFTXM
# uJYNvcAyHwMJwbF

#/html/body/div/div/div[2]/div[2]
#/html/body/div/div/div[2]/div[2]


##kRXSgGUvAFORFDP
