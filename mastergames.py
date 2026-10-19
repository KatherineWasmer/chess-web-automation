from selenium.webdriver.common.by import By
import time

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