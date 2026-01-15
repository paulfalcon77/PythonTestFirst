import pytest
from playwright.sync_api import Page, expect

def test_disabled(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    button = page.locator("#submit-id-submit")
    expect(button).to_be_disabled()
    result = page.locator("#result-text")
    expect(result).not_to_be_visible()

    #pytest --headed tests/qa_practice/test_disabled.py
