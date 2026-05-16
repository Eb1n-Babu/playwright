from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser_1 = playwright.chromium.launch(headless=False , slow_mo=500)
    browser_2 = playwright.firefox.launch(headless=True)
    browser_3 = playwright.webkit.launch()

    context = browser_1.new_context(
        viewport={"width": 640, "height": 640},
        locale="en_US",
        timezone_id="Asia/Tokyo",
    )

    page = context.new_page()
    page.goto("https://playwright.dev")
    page.wait_for_timeout(2000)
    browser_1.close()