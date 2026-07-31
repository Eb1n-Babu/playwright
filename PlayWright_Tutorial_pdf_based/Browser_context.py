"""Concept-In general the playwright tests work on the web browser through the configurations given in the
configuration file.
Below code gives one an option to set the required web browser through the script."""
import asyncio

from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context_1 = await browser.new_context(viewport={'width': 1920, 'height': 1080})#type: ignore
        context_2 = await browser.new_context(viewport={'width': 1920, 'height': 1080})#type: ignore

        page_1 = await context_1.new_page()
        page_2 = await context_2.new_page()

        await page_1.goto('http://google.com')
        await page_2.goto('http://instagram.com')

        await page_1.screenshot(path="./google.png")
        await page_2.screenshot(path="./instagram.png")

        await browser.close()
        await context_1.close()
        await context_2.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

