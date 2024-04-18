from os import system
system('pip install selenium')
system('pip install webdriver_manager')
system('pip install cleantext')
system('cls')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from cleantext import clean

readme = open('README.md', "w")
readme.write('')
readme.close()

## OPTIONS
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)

## INPUT
username = str(input('Scratch Username > '))


## COLLECT DATA
driver.get(f"https://scratch.mit.edu/users/{username}/projects/")

logo = driver.find_element(By.CLASS_NAME, 'portrait')
games = driver.find_elements(By.CLASS_NAME, 'project')

links = []
titles = []

for game in games:
    links.append(str(game.find_element(By.TAG_NAME, 'a').get_attribute('href')))
    titles.append(clean(text=str(game.find_element(By.CLASS_NAME, 'title').text), no_emoji=True, lower=False))

    
## WRITE DATA
readme = open('README.md', "a")
readme.write(f'![Logo](# {username}\'s Scratch Projects\n\n')
for i in range(len(links)):
    print(f'{titles[i]}, {links[i]}')
    readme.write(f'[{titles[i]}]({links[i]})\n')
readme.close()
driver.close()