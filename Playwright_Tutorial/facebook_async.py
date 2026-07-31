from playwright.async_api import async_playwright
import asyncio

async def Home():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)

        page = await browser.new_page()
        await page.goto("https://www.facebook.com")
        await page.wait_for_timeout(200)
        await page.screenshot(path="./facebook_screenshot.png")

        await page.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(Home())