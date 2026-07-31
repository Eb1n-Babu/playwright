from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        context = await browser.new_context(viewport={"width": 1920, "height": 1080})# type: ignore

        page = await context.new_page()
        await page.goto("https://facebook.com")
        await page.wait_for_timeout(200)

if __name__ == '__main__':
    asyncio.run(main())
