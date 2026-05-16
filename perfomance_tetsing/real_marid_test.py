import asyncio
from playwright.async_api import async_playwright

async def run():
    browsers = ["chromium", "firefox", "webkit"]

    async with async_playwright() as p:
        for browser_type in browsers:
            browser = await getattr(p, browser_type).launch()
            context = await browser.new_context()
            page = await context.new_page()

            start = asyncio.get_event_loop().time()
            await page.goto("https://www.realmadrid.com", wait_until="networkidle")
            duration = (asyncio.get_event_loop().time() - start) * 1000  # ms

            print(f"{browser_type} load time: {duration:.2f} ms")

            await browser.close()

asyncio.run(run())
