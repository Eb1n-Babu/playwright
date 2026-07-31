import asyncio

from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})# type: ignore
        page = context.new_page()
        page.goto("https://practice.expandtesting.com/login")
        page.locator("#username").fill("practice")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("#submit-login").click()
        page.wait_for_timeout(2000)

async def main_async():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("#username").fill("practice")
        await page.locator("#password").fill("SuperSecretPassword!")
        await page.locator("#submit-login").click()

        await page.wait_for_timeout(2000)

        await page.close()
        await context.close()
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main_async())

