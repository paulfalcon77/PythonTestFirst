import pytest
from playwright.sync_api import Page

def test_example(page: Page):
    """
    Простой тест: открываем https://example.com и проверяем заголовок.
    """
    page.goto("https://example.com")
    page.screenshot(path="example.png")
    assert "Example Domain" in page.locator("h1").inner_text()