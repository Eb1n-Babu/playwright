from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    webdriver = playwright.chromium.launch(headless=False)
    context = webdriver.new_context(viewport={'width': 1920, 'height': 1080})

    page = context.new_page()
    page.goto("https://www.linkedin.com/")

    page.wait_for_timeout(10000)
    page.close()
    webdriver.close()
