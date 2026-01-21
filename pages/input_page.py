from playwright.sync_api import expect

MESSAGE = "HelloWorld"

RESULT = "#result-text"

class InputIn:
    def __init__(self, page):
        self.page = page
    def open(self):
        self.page.goto("https://www.qa-practice.com/elements/input/simple")

    def simple_input(self):
        input_field = self.page.locator("#id_text_string")
        input_field.fill(MESSAGE)
        input_field.press("Enter")

    def check_result_text_(self, text):
         result = self.page.locator(RESULT)
         expect(result).to_have_text(text)