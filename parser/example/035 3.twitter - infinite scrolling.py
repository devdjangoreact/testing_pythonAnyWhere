from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

web = "https://twitter.com/TwitterSupport/status/1415364740583395328"
# web = "https://twitter.com/TwitterSupport"
path = '/Users/frank/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Get the initial scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(5)
    # Calculate new scroll height and compare it with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # if the new and last height are equal, it means that there isn't any new page to load, so we stop scrolling
        break
    else:
        last_height = new_height

# def get_tweet(element):
#     try:
#         user = element.find_element_by_xpath(".//span[contains(text(), '@')]").text
#         text = element.find_element_by_xpath(".//div[@lang]").text
#         tweet_data = [user, text]
#     except:
#         tweet_data = ['user', 'text']
#     return tweet_data

# user_data = []
# text_data = []
#
# tweets = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']")))
# for tweet in tweets:
#     tweet_list = get_tweet(tweet)
#     user_data.append(tweet_list[0])
#     text_data.append(" ".join(tweet_list[1].split()))

driver.quit()
#
# df_tweets = pd.DataFrame({'user': user_data, 'text': text_data})
# df_tweets.to_csv('tweets.csv', index=False)
# print(df_tweets)
