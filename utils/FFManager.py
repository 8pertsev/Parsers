from selenium import webdriver


class FFManager:

    def __init__(self, url):

        self.ff_options = webdriver.FirefoxOptions()
        self.ff_options.add_argument('--window-size=1820,1000')

        self.url = url

    def __enter__(self):

        self.firefox = webdriver.Firefox(executable_path='F:/geckodriver.exe', options=self.ff_options)
        self.firefox.get(self.url)
        return self.firefox

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.firefox.close()

