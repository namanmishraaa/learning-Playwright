import re

from playwright.sync_api import expect


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