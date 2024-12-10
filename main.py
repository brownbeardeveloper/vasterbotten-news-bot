from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize webdriver and open the website
driver = webdriver.Firefox()
driver.get("https://www.svt.se/")

# deny cookies
cookie_btn = driver.find_element(By.XPATH, "//button[text()='Avvisa alla']")
cookie_btn.click()

# go to the local news
local_btn = driver.find_element(By.XPATH, "//a[@data-title='Lokalt']")
local_btn.click()

# open Västerbotten news
link = driver.find_element(By.XPATH, "//a[text()='Västerbotten']")
link.click()

# Wait for 0.5 seconds to allow the page to load
time.sleep(0.5)

# get all h1 elements from the website
h1_elements = driver.find_elements(By.TAG_NAME, "h1")

#  filter out uppercase titles
filtered_titles = [h1.text for h1 in h1_elements if not h1.text.isupper()]

# Print the text of each <h1> element
for h1 in filtered_titles:
    print(h1)

driver.quit()
