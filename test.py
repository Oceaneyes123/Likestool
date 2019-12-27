from selenium import webdriver
import os
from time import sleep


driver = webdriver.Chrome('C:/Users/Dave/Downloads/Compressed/Compressed/chromedriver_win32/chromedriver.exe')
driver.get("http://legacy.likestool.com/campaign/my-campaigns")
driver.execute_script("document.getElementById('loginform-username').value = 'hideemail2@hideemail.net'; document.getElementById('loginform-password').value = 'oceaneyes0928'; document.getElementById('login_form').submit(); ")
sleep(10)
driver.get("http://legacy.likestool.com/campaign/add-site-form")
driver.execute_script("document.getElementById('campaign-type').value = '17'; document.getElementById('campaign-title').value = 'Subzz'; document.getElementById('campaign-url').value = 'https://www.youtube.com/channel/UC0G4Xh0DTGeqZxAVX66WATw'; document.getElementById('add_edit').submit();")
