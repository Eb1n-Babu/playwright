from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto("https://www.google.com")
    page.locator("#APjFqb").fill("abc")
    page.wait_for_timeout(1000)
    page.close()
    context.close()
    browser.close()

