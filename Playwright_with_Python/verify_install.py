import time

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser_1 = playwright.chromium.launch(headless=True)
    browser_2 = playwright.webkit.launch(headless=True)
    browser_3 = playwright.firefox.launch(headless=True)

    page_1 = browser_1.new_page()
    start = time.time()
    page_1.goto("https://www.realmadrid.com/en-US")
    page_1.wait_for_load_state()
    end = time.time()
    print(f"Page Load Time: {end - start:.2f} seconds")
    print(page_1.title())
    browser_1.close()


    page_2 = browser_2.new_page()
    start = time.time()
    page_2.goto("https://www.realmadrid.com/en-US")
    page_2.wait_for_load_state()
    end = time.time()
    print(f"Page Load Time: {end - start:.2f} seconds")
    print(page_2.title())
    browser_2.close()


    page_3 = browser_3.new_page()
    start = time.time()
    page_3.goto("https://www.realmadrid.com/en-US")
    page_3.wait_for_load_state()
    end = time.time()
    print(f"Page Load Time: {end - start:.2f} seconds")
    print(page_3.title())
    browser_3.close()