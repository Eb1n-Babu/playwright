from playwright.sync_api import sync_playwright



def load_dc_books():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width':800,'height':600})
        page = context.new_page()
        page.goto("https://dcbookstore.com/")
        page.get_by_text("Login").click()
        page.get_by_placeholder("User Name").fill("wacot15348@badgerhole.com")
        page.get_by_placeholder("Password").fill(".}5@duj4Wy?=;]P")
        page.get_by_role("button",name="LOGIN").click()
        page.wait_for_timeout(1000)
        page.go_back()
        page.wait_for_timeout(1000)

        page.close()
        context.close()
        browser.close()


load_dc_books()