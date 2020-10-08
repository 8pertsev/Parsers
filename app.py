from selenium import webdriver
from pages.flamp_page import FlampPage
from utils.url_click import UrlClick
from utils.page_scroll import PageScroll
from utils.FFManager import FFManager

import time


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--window-size=1820,1000')
# chrome_options.headless = True

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


with FFManager('https://novosibirsk.flamp.ru/firm/shashlykoff_gril_bar-141265770259834') as ff_browser:
    page = FlampPage(ff_browser)

    url_click = UrlClick()
    time.sleep(3)
    url_click.click_nohrefs(ff_browser, 'Показать ещё отзывы')
    time.sleep(3)
    url_click.click_nohrefs(ff_browser, 'Показать целиком')

    for i in page.search_for_reviews():
        print(i)

    while True:
        time.sleep(3)
        PageScroll.page_scroll(ff_browser, 3)
        url_click.click_nohrefs(ff_browser, 'Показать целиком')
        time.sleep(3)
        for i in page.search_for_scroll_5_reviews():
            print(i)
        time.sleep(3)
