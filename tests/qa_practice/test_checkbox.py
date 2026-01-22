from playwright.sync_api import Page, expect

def test_checkbox_clicked(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    checkbox_field = page.locator("#id_checkbox_0")
    checkbox_field.click()
    button = page.locator("#submit-id-submit")
    button.click()
    result = page.locator("#result-text")
    expect(result).to_have_text("select me or not")


#pytest --headed  tests/qa_practice/test_checkbox.py