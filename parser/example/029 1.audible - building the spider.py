from selenium import webdriver
import pandas as pd

web = "https://www.audible.com/search"
path = '/Users/frank/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()

# Locating the box that contains all the audiobooks listed in the page
container = driver.find_element_by_class_name('adbl-impression-container ')
# Getting all the audiobooks listed (the "/" gives immediate child nodes)
products = container.find_elements_by_xpath('./li')
# Initializing storage
book_title = []
book_author = []
book_length = []
# Looping through the products list (each "product" is an audiobook)
for product in products:
    # We use "contains" to search for web elements that contain a particular text, so we avoid building long XPATH
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)  # Storing data in list
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
