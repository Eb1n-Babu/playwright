from playwright.async_api import async_playwright
import asyncio

async def Home():
    async with async_playwright() as playwright:

        browser = await playwright.chromium.launch(headless=True)

        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})

        page = await context.new_page()
        await page.goto("https://linkedin.com")
        await page.screenshot(path="./linkedin_screenshot.png")

        await page.close()
        await context.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(Home())


