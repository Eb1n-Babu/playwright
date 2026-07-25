from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"height": 1920, "width": 1080})
        page = await context.new_page()
        await page.goto("https://www.google.com")
        await page.locator("#APjFqb").fill("abc")
        await page.wait_for_timeout(1000)
        await page.close()
        await context.close()
        await browser.close()

asyncio.run(main())

