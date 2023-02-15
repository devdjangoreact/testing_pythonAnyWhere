from selenium import webdriver
import time
import os

web = "https://twitter.com/"
path = "/Users/frank/Downloads/chromedriver"
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# locating and clicking the login button
login = driver.find_element_by_xpath('//a[@href="/login"]')
login.click()
time.sleep(2)

# getting the login box that contains the username and password
login_box = driver.find_element_by_xpath('//form[@action="/sessions"]')

# locating username and password inputs
username = login_box.find_element_by_xpath('.//input[@name="session[username_or_email]"]')
password = login_box.find_element_by_xpath('.//input[@name="session[password]"]')

# sending text to the inputs
username.send_keys("Write Email Here")
password.send_keys("Write Password Here")
# username.send_keys(os.environ.get("TWITTER_USER"))
# password.send_keys(os.environ.get("TWITTER_PASS"))

# locating login button and then clicking on it
login_button = driver.find_element_by_xpath('//div[@role="button"]')
login_button.click()

# closing driver
# driver.quit()
