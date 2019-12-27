from selenium.webdriver import ChromeOptions
from splinter import Browser
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from halo import Halo



browser.visit("http://legacy.likestool.com/")
browser.fill('LoginForm[username]', 'hideemail2@hideemail.net')
browser.fill('LoginForm[password]', 'oceaneyes0928')
browser.find_by_xpath('//*[@id="login_form"]/div[4]/input').click()
sleep(10)
browser.visit("http://legacy.likestool.com/campaign/add-site-form")
element = browser.find_by_id('campaign-type').first
element.select('17')
browser.fill('Campaign[title]', 'Subzz')
browser.fill('Campaign[url]', 'https://www.youtube.com/channel/UC0G4Xh0DTGeqZxAVX66WATw')
browser.find_by_xpath('//*[@id="add_edit"]/div[4]/input').click()

