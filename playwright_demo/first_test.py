from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        base_url = "https://www.saucedemo.com/inventory.html"
        page.goto(base_url)
        page.wait_for_timeout(5000)  # wait for 5 seconds to ensure page loads
        print("Page title:", page.title())
        browser.close()


if __name__ == "__main__":
    run()

