from selenium import webdriver
from pages.flamp_page import FlampPage
from utils.url_click import UrlClick
from utils.page_scroll import PageScroll

import time


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--window-size=1820,1000')
# chrome_options.headless = True
ff_options = webdriver.FirefoxOptions()
ff_options.add_argument('--window-size=1820,1000')

# try:
#     author = input("Enter the author you'd like quotes from: ")
#     tag = input("Enter your tag: ")
#
#     # chrome = webdriver.Chrome(executable_path='C:/work/chromedriver.exe', options=chrome_options)
#     # chrome.create_options()
#     chrome.get('http://quotes.toscrape.com/search.aspx')
#     page = QuotesPage(chrome)
#
#     print(page.search_for_quotes(author, tag))
#     chrome.stop_client()
#     chrome.quit()
#
# except InvalidTagForAuthorError as e:
#     print(e)
# except Exception:
#     print("An unknown error occurred. Please try again.")

# try:
# chrome = webdriver.Chrome(executable_path='C:/work/chromedriver.exe', options=chrome_options)
# chrome.create_options()
# chrome.get('https://novosibirsk.flamp.ru/firm/shashlykoff_gril_bar-141265770259834')
# page = FlampPage(chrome)

firefox = webdriver.Firefox(executable_path='F:/geckodriver.exe', options=ff_options)

firefox.get('https://novosibirsk.flamp.ru/firm/shashlykoff_gril_bar-141265770259834')
page = FlampPage(firefox)

url_click = UrlClick()
time.sleep(3)
url_click.click_nohrefs(firefox, 'Показать ещё отзывы')
time.sleep(3)
url_click.click_nohrefs(firefox, 'Показать целиком')

for i in page.search_for_reviews():
    print(i)

while True:
    time.sleep(3)
    PageScroll.page_scroll(firefox, 3)
    url_click.click_nohrefs(firefox, 'Показать целиком')
    time.sleep(3)
    for i in page.search_for_scroll_5_reviews():
        print(i)
    time.sleep(3)

# except Exception:
#     print("An unknown error occurred. Please try again.")
# chrome.stop_client()
# chrome.quit()