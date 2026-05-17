from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        locale="en_US",
        timezone_id="Asia/Seoul"
    )

    page = context.new_page()
    page.goto("http://localhost:63343/Playwright_with_Python/practise.html")
    page.wait_for_timeout(5000)

    # Login
    page.get_by_label("Username").fill("myuser")
    page.get_by_label("Password").fill("pass123")
    page.get_by_role("button", name="Login").click()

    # Checkboxes, radio, select
    page.get_by_role("checkbox").check()
    page.get_by_role("radio").check()
    page.select_option("select#country", "India")

    # Keyboard & Mouse
    page.keyboard.press("Enter")
    page.locator("canvas").click(position={"x": 100, "y": 200})

    # Search with delay
    page.get_by_label("Search").fill("Python", delay=100)

    # Cleanup
    page.close()
    context.close()
    browser.close()
