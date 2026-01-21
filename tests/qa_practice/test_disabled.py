import pytest
from playwright.sync_api import Page, expect
from pages.disabled_page import DisabledPage



def test_disabled(page: Page):
    deactivate = DisabledPage(page)
    deactivate.open()
    deactivate.deactivate()


#pytest --headed  tests/qa_practice/test_disabled.py