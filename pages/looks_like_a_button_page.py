from playwright.sync_api import expect

BUTTON = ".a-button"

RESULT = '.result-text'

class LooksLikeAButton:

    def __init__(self, page):
            self.page = page

    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/button/like_a_button")

    def looks_like_a_button_exist(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def looks_like_a_button_clicked(self):
        button = self.page.locator(BUTTON)
        button.click()

    def check_result_text_is_(self, text):
        result = self.page.locator(RESULT)
        expect(result).to_have_text(text)