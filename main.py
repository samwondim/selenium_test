from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

from homepage.open import *
from homepage.signup import *
from homepage.signin import *
from shared.broken_link_check import *

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

open_homepage(driver)
# check_broken_link(driver)

# signup_test(driver)

signin_test(driver) # hcaptcha automation not implemented. solve it manually!
# check_broken_link(driver)

# tasks after signed in will be procced blow


# all tasks are completed
print("All tasks are completed")
time.sleep(10)
