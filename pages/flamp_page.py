from typing import List
from locators.flamp_review_page_locators import FlampReviewPageLocators
from parsers.flamp import FlampParser


class FlampPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def reviews(self) -> List[FlampParser]:
        return [
            FlampParser(e)
            for e in self.browser.find_elements_by_css_selector(
                FlampReviewPageLocators.CONTENT_LOCATOR
            )
        ]

    def search_for_reviews(self) -> List[FlampParser]:

        return self.reviews

    def search_for_scroll_5_reviews(self) -> List[FlampParser]:

        return self.reviews[-6:-1]


