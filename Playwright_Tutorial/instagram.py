from playwright.sync_api import  sync_playwright
def Home():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)

        context = browser.new_context(viewport={"width": 1920, "height": 1080})  # type: ignore

        page = context.new_page()
        page.goto("https://www.instagram.com/")
        page.wait_for_timeout(200)
        page.screenshot(path="./instagram.png")

        page.close()
        context.close()
        browser.close()

if __name__ == '__main__':
    Home()

