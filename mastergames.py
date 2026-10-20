from selenium.webdriver.common.by import By
import time

# TO-DO: troubleshoot why this script only downloads the first page or doesn't download at all 

def get_total_pages(my_driver):
    return int(my_driver.find_element(By.ID, "master-games-container").get_attribute("data-total-pages"))

def download_games(my_driver):
    time.sleep(10)
    checkbox = my_driver.find_element(By.ID, "master-games-check-all")
    checkbox.click() 
    time.sleep(3)
    download = my_driver.find_element(By.CLASS_NAME, "master-games-download-button")
    download.click()

def get_next_button(my_driver):
    my_driver.execute_script("window.scrollBy(500, 5000);")
    next_button = my_driver.find_element(By.CSS_SELECTOR, '[aria-label = "Next Page"]')
    next_button.click() 

def download_player_games(my_driver, players_list):
    for player in players_list:
        num_names = len(player.split(" "))
        hyphenated_name = ""
        for i in range(num_names):
            hyphenated_name += player.split(" ")[i]
            if i < num_names - 1:
                hyphenated_name += "-"
        my_driver.get(f"http://www.chess.com/games/{hyphenated_name}")
        my_driver.execute_script("window.scrollBy(0, 500);")
        pages = get_total_pages(my_driver)

        i = 0 
        while i < pages:
            print(my_driver.current_url)
            my_driver.execute_script("window.scrollBy(0, 500);")
            download_games(my_driver)
            get_next_button(my_driver)
            i += 1

        my_driver.quit()
