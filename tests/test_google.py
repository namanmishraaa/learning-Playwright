import re
from playwright.sync_api import expect

def test_google_search(page):

    # Go to Google
    page.wait_for_timeout(5000)  # wait for 5 seconds to ensure page loads
    page.goto("https://www.google.com/ncr")
    try :
        # Accept cookies popup
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except :
        # If no popup, continue
        print("NO Popup!")

    # Perform search and press Enter on keyboard
    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)

    # Verify search results page
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))

