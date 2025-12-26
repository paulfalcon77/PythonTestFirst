import logging
import pytest
import re
from playwright.sync_api import Page, expect


def test_login_failure(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    logging.info('Web checked')

    page.locator('id=username').fill('tomsmith')
    logging.info('username is checked')
    page.locator('id=password').fill('SuperSecretPassword!')
    logging.info('password is checked')

    page.get_by_role("button", name="Login").click()
    logging.info('button is pushed')

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    logging.info("URL is changed /secure")

    success_banner = page.locator(".flash.success")
    expect(success_banner).to_be_visible()
    expect(success_banner).to_contain_text("You logged into a secure area!")
    logging.info("Текст об успешном входе найден")


