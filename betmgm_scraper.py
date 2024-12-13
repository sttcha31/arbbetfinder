import multiprocessing
import csv
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
    

def get_player_overunder(link, category):
    overunders = []
    driver = webdriver.Chrome(options=op)
    driver.get(link+"?market=Players:"+category)
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-option-panel-bottom-action/div')))
    button.click()

    table = driver.find_element(By.XPATH, '//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-split-header/div')

    content = table.find_elements(By.XPATH, "./*")
    for i in range(1, len(content)):
        overunder = {}
        overunder["sportsbook"] = "BetMGM"
        overunder["player_name"] = content[i].find_element(By.CLASS_NAME, "player-props-player-name").text
        overunder["category"] = category
        overunder["value"]= content[i].find_element(By.CLASS_NAME, "option-pick").find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "name").text[2:]
        overunder["over"] = content[i].find_elements(By.CLASS_NAME, "option-pick")[0].find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        overunder["under"]= content[i].find_elements(By.CLASS_NAME, "option-pick")[1].find_element(By.CLASS_NAME, "option-indicator").find_element(By.CLASS_NAME, "value").find_element(By.TAG_NAME, 'ms-font-resizer').find_element(By.CLASS_NAME, "custom-odds-value-style").text
        overunders.append(overunder)
    print(overunders)
    write_to_csv(overunders)

def process_task(task):
    link, category = task
    get_player_overunder(link, category)

def write_to_csv(data):
    with open("odds.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)

if __name__ == '__main__':
    headers = ["sports_book", "player_name", "category", "value", "over", "under"]
    with open("odds.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    tasks = list()
    tasks.append(("https://sports.va.betmgm.com/en/sports/events/new-orleans-pelicans-at-houston-rockets-16687910", "Points"))
    tasks.append(("https://sports.va.betmgm.com/en/sports/events/new-orleans-pelicans-at-houston-rockets-16687910", "Assists"))
    tasks.append(("https://sports.va.betmgm.com/en/sports/events/new-orleans-pelicans-at-houston-rockets-16687910", "Rebound"))
    tasks.append(("https://sports.va.betmgm.com/en/sports/events/new-orleans-pelicans-at-houston-rockets-16687910", "ThreePointer"))
    with multiprocessing.Pool(processes=len(tasks)) as pool:
        results = pool.map(process_task, tasks)

