import pytest
from playwright.async_api import Playwright, Browser


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with Playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


def test_sample(playwright_instance: Browser):
    page = playwright_instance.new_page()
    page.goto("https://www.google.com")
    assert "Google" in page.title()

