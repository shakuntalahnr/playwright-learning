import pytest
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page : Page, base_url):
        self.page = page
        self.base_url = base_url
        self.username = page.get_by_test_id("username")
        self.password = page.get_by_test_id("password")
        self.login = page.get_by_role("button", name="Login")
        
        
