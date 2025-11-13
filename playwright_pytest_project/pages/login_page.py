"""
convert the following code to a playwright page object model for a login page in python using pytest framework:-
def test_example(page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(r"^Username$")).nth(2)).to_be_visible()
    expect(page.get_by_text("Password", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.locator("span").filter(has_text="firstname lastname").click()
    page.get_by_role("menuitem", name="Logout").click()
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
    expect(page.locator("div").filter(has_text=re.compile(r"^Dashboard$"))).to_be_visible()
    page.get_by_role("heading", name="Dashboard").click()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

"""

import re
from playwright.sync_api import expect


class LoginPage:

    """
    Page Object Model for the Login Page.
    """

    USERNAME_LOCATOR = "textbox[name='Username']"
    PASSWORD_LOCATOR = "textbox[name='Password']"
    LOGIN_BUTTON_LOCATOR = "button[name='Login']"
    HEADING_LOCATOR = "heading[name='Login']"

    def __init__(self, page):
        self.page = page

    def username(self, username="Admin"):
        """
        :param username: enter the username to login
        :return:
        """
        self.page.get_by_role("textbox", name="Username").click()
        self.page.get_by_role("textbox", name="Username").fill(username)

    def password(self, password="admin123"):
        """
        :param password: enter the password to login
        :return:
        """
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(password)

    def click_login(self):
        """
        Click on the login button
        :return:
        """
        self.page.get_by_role("button", name="Login").click()

    def verify_login_page(self):
        """
        Verify the login page elements
        :return:
        """
        expect(self.page.get_by_role("heading", name="Login")).to_be_visible()
        expect(self.page.locator("div").filter(has_text=re.compile(r"^Username$")).nth(2)).to_be_visible()
        expect(self.page.get_by_text("Password", exact=True)).to_be_visible()
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()

    def verify_username(self, username):
        pass

    def verify_successful_login(self):
        """
        Verify successful login by checking for the Dashboard heading
        :return:
        """
        expect(self.page.locator("div").filter(has_text=re.compile(r"^Dashboard$"))).to_be_visible()
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()


