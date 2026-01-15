import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.wait_for_timeout(2000)
    expect(page).to_have_title(re.compile("QA Practice"))
    print("\n[SUCCESS] Title is correct!")
    description = page.locator("p").first
    expect(description).to_contain_text("This site is designed")
    print("\n[SUCCESS] Text is correct!")

#def test_has_description(page: Page):
 #   page.goto("https://www.qa-practice.com/")

#pytest --headed --slowmo 2000 tests/qa_practice/test_first.py
#