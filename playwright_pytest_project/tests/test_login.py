"""
This script tests the login functionality of a web application using Playwright and pytest. It defines a LoginPage class
that encapsulates the interactions with the login page, including entering the username and password, clicking the login
button, and verifying the presence of the login heading.
"""

import re
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_page(page):
    login_page = LoginPage(page)

    # Navigate to the login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Verify the login page elements are visible
    login_page.verify_login_page()

    # Enter username and password
    login_page.username("Admin")
    login_page.password("admin123")

    # Click the login button
    login_page.click_login()

    # Verify successful login by checking for the Dashboard heading
    login_page.verify_successful_login()

    # Logout process
    page.get_by_role("banner").get_by_role("img", name="profile picture").click()
    page.get_by_role("menuitem", name="Logout").click()

    # Verify that we are back on the login page
    login_page.verify_login_page()