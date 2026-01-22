from playwright.sync_api import Page, expect

def test_checkboxes_clicked(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    cb_one = page.locator("#id_checkboxes_0")
    cb_tree = page.locator("#id_checkboxes_2")
    cb_one.check()
    cb_tree.check()
    button = page.locator("#submit-id-submit")
    button.click()
    result = page.locator("#result-text")
    expect(result).to_contain_text("one, three")

    # pytest --headed  tests/qa_practice/test_checkboxes.py
