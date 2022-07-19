from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://google.com/search?q=amazon+ratenzahlung')


consent_button = driver.find_element(By.ID, "L2AGLb")
consent_button.click()
time.sleep(2)

pagenumber = 1
resultsnumber = 0

try:
    while resultsnumber <= 100:
        search = driver.find_element(By.ID, "search")
        results = search.find_elements(By.CLASS_NAME, "Ww4FFb")
        resultsnumber = resultsnumber + len(results)
        for Ww4FFb in results:
            heading = Ww4FFb.find_element(By.CLASS_NAME, "LC20lb")
            link = Ww4FFb.find_element(By.TAG_NAME, "a")
            href = link.get_attribute('href')
            print(heading.text, href)
        navigation = driver.find_element(By.CLASS_NAME, "AaVjTc")
        pagenumber = pagenumber + 1
        pnr = str(pagenumber)
        navigation.find_element(By.LINK_TEXT, pnr).click()

        if resultsnumber >= 100:
            print('------ Reached 100 Results ------')
            driver.quit()
except:
    driver.quit()
