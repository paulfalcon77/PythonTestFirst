from playwright.sync_api import Page, expect

def test_simple_input(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_field = page.locator("#id_text_string")
    input_field.fill("HelloWorld")
    input_field.press("Enter")
    result = page.locator("#result-text")
    expect(result).to_have_text("HelloWorld")