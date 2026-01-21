from playwright.sync_api import expect

BUTTON = "#submit-id-submit"

RESULT = "#result-text"


class DisabledPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/button/disabled")

    def deactivate(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_disabled()
        result = self.page.locator(RESULT)
        expect(result).not_to_be_visible()