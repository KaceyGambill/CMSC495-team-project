from helium import *
import selenium
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome("/Users/michaelgalyen/Documents/SDEV_495/project_v1/CMSC495-team-project/chromedriver", chrome_options=options)



url = "https://www.freecodecamp.org/news/tag/interview"

#PATH_TO_CHROMEDRIVER = '/Users/michaelgalyen/Documents/SDEV_495/project_v1/CMSC495-team-project/chromedriver'

#driver = selenium.webdriver.Chrome(PATH_TO_CHROMEDRIVER)

browser = start_chrome(url)

# html = browser.page_source
#
# print(html)