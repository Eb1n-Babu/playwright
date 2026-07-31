from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={'width': 800, 'height': 600})

    page = context.new_page()
    page.goto("https://iqvia.wd1.myworkdayjobs.com/IQVIA/login")
    page.locator("#input-4").fill("username")
    page.locator("#input-5").fill("password")
    #page.get_by_role("button",name="Sign In").click()
    page.wait_for_timeout(10000)