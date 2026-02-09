from playwright.sync_api import Page, expect

from pages.input_page import InputIn


def test_simple_input(page: Page):
    simple_input = InputIn(page)
    simple_input.open()
    simple_input.simple_input()
    simple_input.check_result_text_("HelloWorld!")


#update
#pytest --headed  tests/qa_practice/test_input.py