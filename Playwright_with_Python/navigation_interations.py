from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    new_browser = playwright.chromium.launch(headless=False)  # show browser
    context = new_browser.new_context(
        viewport={"width": 640, "height": 480},
        locale="en_US",
        timezone_id="Asia/Seoul",
    )
    page = context.new_page()
    page.goto("https://www.realmadrid.com/")
    page.goto("https://www.fcbarcelona.com/en/")
    page.go_back()
    page.wait_for_load_state("load")
    page.go_forward()
    page.reload()
    page.wait_for_timeout(2000)

    print(page.title)
    print(page.url)

    # Proper cleanup
    page.close()
    context.close()
    new_browser.close()
