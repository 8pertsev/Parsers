import time


class PageScroll:

    @staticmethod
    def page_scroll(browser, timeout):

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(timeout)
