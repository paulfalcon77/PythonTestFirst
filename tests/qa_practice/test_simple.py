import pytest
from playwright.sync_api import Page, expect

def test_simple_is(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    simple_button = page.get_by_role('link', name='Simple button')
    expect(simple_button).to_be_visible()
    button = page.locator('.a-button')
    expect(button).to_be_visible()

def test_simple_clicked(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/like_a_button")
    button = page.locator('.a-button')
    button.click()
    result = page.locator('#result')
    expect(result).to_have_text('Submitted')




#pytest --headed  tests/qa_practice/test_simple.py