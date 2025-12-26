from playwright.sync_api import Page, expect
import pytest, logging
def test_checkboxes_visual(page: Page):

    page.goto("https://the-internet.herokuapp.com/checkboxes")
    logging.info("Checkbox is opened")

    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)

    logging.info(f"Before: Checkbox1 = {checkbox1.is_checked()}, Checkbox2 = {checkbox2.is_checked()}")

    checkbox1.check()
    logging.info("Put the sign in the checkbox1")

    checkbox2.uncheck()
    logging.info("Take off the sign in the checkbox2")

    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()

    page.wait_for_timeout(3000)