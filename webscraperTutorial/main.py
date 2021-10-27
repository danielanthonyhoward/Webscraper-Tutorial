#IMPORTS
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

#WEB DRIVER
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

#INITIALIZE TABLES
title = []
time_span = []
country = []
id = []
teaser = []
last_update = []

#INITIALIZE PAGE

page = 0

#SCRAPER

while page == 0:

    page = page + 1
    url = 'https://cordis.europa.eu/search?q=contenttype%3D%27project%27%20AND%20applicationDomain%2Fcode%3D%27ener%27%20AND%20(programme%2Fcode%3D%27H2020%27)&p={}&num=100&srt=Relevance:decreasing'.format(page)

    try:

        driver.get(url)
        time.sleep(20)

        projects = driver.find_elements(By.CSS_SELECTOR,'#c-main > div > div > section.o-section.col.c-search__container > section.c-search__results.ng-star-inserted > app-card-search > div > div.col-lg.c-card-search__content-side')

        if len(projects) == 0:
            print(page)
            break

        for project in projects:
            _id = project.find_element(By.CSS_SELECTOR,'#c-main > div > div > section.o-section.col.c-search__container > section.c-search__results.ng-star-inserted > app-card-search > div > div.col-lg.c-card-search__content-side > div.c-card-search__block > p.c-card-search__line.col-12.col-lg-5.ng-star-inserted').text
            _country = 'Denmark'


            id.append(_id)
            country.append(_country)


    except:
        break

data = {'Id':id,
        'Country': country}

#DATAFRAME

df_projects = pd.DataFrame(data)
print(df_projects.head())

#EXPORT

#df_projects.to_csv(r'path\filename.csv', index = False, header=True)




