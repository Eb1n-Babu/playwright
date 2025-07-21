from playwright.sync_api import sync_playwright


def playwrightDemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.realmadrid.com/en-US")
        print("page title",page.title())
        page.screenshot(path=r"./screenshot.png")
        print("Screenshot saved as screenshot.png" )
        browser.close()

if __name__ == '__main__':
    playwrightDemo()