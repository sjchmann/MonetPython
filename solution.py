from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://google.com/')

queries = ['amazon ratenzahlung', 'h&m ratenzahlung', 'otto ratenzahlung', 'amazon rechnungskauf', 'mediamarkt ratenzahlung']
queries_no = len(queries) - 1
i = 0

consent_button = driver.find_element(By.ID, "L2AGLb")
consent_button.click()
time.sleep(2)

while i <= queries_no:
    query = driver.find_element(By.NAME, "q")
    query.clear()
    query.send_keys(queries[i])
    query.send_keys(Keys.RETURN)
    print("Searching:", queries[i])

    search = driver.find_element(By.ID, "search")
    results = search.find_elements(By.CLASS_NAME, "Ww4FFb")
    result = results[0]

    heading = result.find_element(By.CLASS_NAME, "LC20lb")
    link = result.find_element(By.TAG_NAME, "a")
    href = link.get_attribute('href')
    print(heading.text)
    print(href)
    print('-------------------------------')

    i = i + 1
driver.quit()
