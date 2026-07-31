from playwright.async_api import async_playwright
import  asyncio

async def main():
    async with async_playwright() as playwright:
        webdriver = await playwright.chromium.launch(headless=False)
        context = await webdriver.new_context()

        page = await context.new_page()
        await page.goto("https://www.linkedin.com/")

        await page.wait_for_timeout(20000)
        await page.close()
        await webdriver.close()

asyncio.run(main())

