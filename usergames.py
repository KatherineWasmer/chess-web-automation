from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_chess_profile(my_driver, user):
    my_driver.get(f"http://www.chess.com/member/{user}/games")
    time.sleep(1)

def check_all_games(my_driver):
    checkbox = WebDriverWait(my_driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Select All']"))
    )
    checkbox.click() 
    time.sleep(1)