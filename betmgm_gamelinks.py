import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
op = webdriver.ChromeOptions()
# op.add_argument('--headless')
# op.add_argument("--window-size=1920,1080")
# op.add_argument('--disable-gpu')
# op.add_argument('--no-sandbox')
op.add_argument("--enable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")
op.add_argument("--enable-javascript")

def get_game_links():
    driver = webdriver.Chrome(options=op)
    driver.get("https://sports.mi.betmgm.com/en/sports/basketball-7/betting/usa-9/nba-6004")
    wait = WebDriverWait(driver, 20)
    #CHECK: following line's XPATH might chance from day to day
    output = list()                                                
    driver.get_screenshot_as_file("screenshot.png")
    table = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ms-widget-layout/ms-widget-slot/ms-composable-widget/ms-widget-slot/ms-tabbed-grid-widget/ms-grid/div/ms-event-group')))
    games = table.find_elements(By.XPATH, "./*")
    with open("mgmgames.txt", "w") as file: 
        for game in games:
            file.write(game.find_element(By.CLASS_NAME, "grid-event-wrapper").find_element(By.TAG_NAME, "a").get_attribute("href") + "\n")
            output.append(game.find_element(By.CLASS_NAME, "grid-event-wrapper").find_element(By.TAG_NAME, "a").get_attribute("href") + "\n")
    return output

get_game_links()