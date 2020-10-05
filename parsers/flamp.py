from locators.flamp_review_locators import FlampReviewLocators
from locators.flamp_review_page_locators import FlampReviewPageLocators
from utils.url_click import UrlClick


class FlampParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<{self.author}, {self.date}, рейтинг: {self.rating}, {self.review}.>"

    @property
    def review(self):
        url_click = UrlClick()
        review = ''
        locator = FlampReviewLocators.REVIEW_LOCATOR_FULL
        for e in self.parent.find_elements_by_css_selector(locator):

            review = review + e.text + "\n"
        # review = review[0: -17]
        return review

    @property
    def author(self):
        locator = FlampReviewLocators.AUTHOR_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def rating(self):
        locator = FlampReviewLocators.RATING_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def date(self):
        locator = FlampReviewLocators.DATE_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def is_expand_button(self):
        locator = FlampReviewPageLocators.TEXT_EXPAND_BUTTON
        try:
            if self.parent.find_element_by_css_selector(locator).text:
                return "ЕСТЬ КНОПКА"
        except Exception:
            return "НЕТ КНОПКИ"
