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


def get_player_overunder(link, category):
    overunders = []
    driver = webdriver.Chrome(options=op)
    driver.get(link+"?market=Players:"+category)
    wait = WebDriverWait(driver, 20)
    if category == "ThreePointer":
        button = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ng-component/div/ms-option-group-list/div/ms-option-panel/div/ms-player-props-option-group/ms-option-panel-bottom-action/div')))
    else:
        button = wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-option-panel-bottom-action/div')))
    button.click()

    table = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/div/ms-player-props-option-group/ms-split-header/div')))
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
    with open("mgmgames.txt", mode="r") as links:
        
        for link in links:
            tasks = list()
            tasks.append((link, "Points"))
            tasks.append((link, "Assists"))
            tasks.append((link, "Rebound"))
            tasks.append((link, "ThreePointer"))
            with multiprocessing.Pool(processes=len(tasks)) as pool:
                results = pool.map(process_task, tasks)

