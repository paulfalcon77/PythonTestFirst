from playwright.sync_api import expect

BUTTON = '.a-button'

RESULT = '#result-text'

class SimplePage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/button/like_a_button")

    def simple_button_exists(self):


        simple_page = SimplePage(self.page)
        simple_button = self.page.get_by_role('link', name='Simple button')
        expect(simple_button).to_be_visible()
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def click_simple_button(self):
        simple_page = SimplePage(self.page)
        button = self.page.locator(BUTTON)
        button.click()
    def check_result_text_is_(self, text):
        result = self.page.locator(RESULT)
        expect(result).to_have_text(text)