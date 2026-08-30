import pytest
from playwright.sync_api import Page, expect

def test_shopping_cart_workflow(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    