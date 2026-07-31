from playwright.sync_api import sync_playwright

def Home():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_timeout(200)
        page.screenshot(path="./google.png")
        page.close()
        browser.close()

if __name__ == '__main__':
    Home()