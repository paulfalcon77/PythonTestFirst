import pytest
from playwright.sync_api import Page, expect
from pages.simple_page import SimplePage

def test_simple_is(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.simple_button_exists()


def test_simple_clicked(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.click_simple_button()
    simple_page.check_result_text_is_('Submitted')




#pytest --headed  tests/qa_practice/test_simple.py