#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    browser = webdriver.Firefox()
    browser.get('https://clickcounter.io/')
    elem = browser.find_element(By.XPATH, '//*[@id="up"]')
    i = 0
    while i < 2023:
        elem.click()
        i += 1
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
