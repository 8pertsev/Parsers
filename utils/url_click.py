from selenium.common.exceptions import ElementNotInteractableException


class UrlClick:

    # click text objects without "href" property
    def click_nohrefs(self, wdriver, text_to_click: str):
        button_clicker = wdriver.find_elements_by_xpath(f"//*[contains(text(), '{text_to_click}')]")

        if button_clicker:

            for e in button_clicker:
                try:
                    e.click()
                except ElementNotInteractableException:
                    print('*** no or no more visible elements ***')
        else:
            print('there were no buttons')


