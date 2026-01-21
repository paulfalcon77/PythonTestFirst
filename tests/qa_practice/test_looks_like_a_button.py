import pytest
from playwright.sync_api import Page, expect
from pages.looks_like_a_button_page import LooksLikeAButton


def test_looks_like_a_button(page: Page):
    like_button = LooksLikeAButton(page)
    like_button.open()
    like_button.looks_like_a_button_exist()


def test_looks_like_a_button_clicked(page: Page):
    like_button = LooksLikeAButton(page)
    like_button.open()
    like_button.looks_like_a_button_clicked()
    like_button.check_result_text_is_('Submitted')


# pytest --headed --slowmo 2000 tests/qa_practice/test_looks_like_a_button.py

#pytest --headed  tests/qa_practice/test_looks_like_a_button.py