import asyncio

from playwright.sync_api import  sync_playwright
from playwright.async_api import async_playwright

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080},
                                      locale='en_US.UTF-8',
                                      timezone_id="Asia/Seoul")
        page = context.new_page()
        page.goto("https://www.google.com")
        page.wait_for_timeout(10000)

#if __name__ == "__main__":
    #main()

async def enabled_inputs():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            locale='en-US',
            timezone_id="Asia/Seoul")
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await page.wait_for_timeout(10000)

asyncio.run(enabled_inputs())


