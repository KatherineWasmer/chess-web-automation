from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
import mastergames as mg 
import usergames as ug

driver = uc.Chrome()

ug.find_chess_profile(driver, "hebeccararis")
ug.check_all_games(driver)