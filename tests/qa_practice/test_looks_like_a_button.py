import pytest
from playwright.sync_api import Page, expect

def test_looks_like_a_button(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    button = page.locator(".a-button")
    expect(button).to_be_visible()

def test_looks_like_a_button_clicked(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    button = page.locator(".a-button")
    button.click()
    result = page.locator('.result-text')
    expect(result).to_have_text('Submitted')

# pytest --headed --slowmo 2000 tests/qa_practice/test_looks_like_a_button.py