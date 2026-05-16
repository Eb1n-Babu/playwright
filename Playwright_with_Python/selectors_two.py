from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as playwright:
        browser_demo = await playwright.chromium.launch(headless=False)
        context = await browser_demo.new_context(viewport={'width':800,'height':600})
        page = await context.new_page()

        await page.goto("https://dcbookstore.com/")
        await page.get_by_text("Login").click()
        await page.get_by_placeholder("User Name").fill("wacot15348@badgerhole.com")
        await page.get_by_placeholder("Password").fill(".}5@duj4Wy?=;]P")
        await page.get_by_role("button", name="LOGIN").click()
        await page.wait_for_timeout(1000)
        await page.go_back()
        await page.wait_for_timeout(1000)

        await page.close()
        await context.close()
        await browser_demo.close()


asyncio.run(main())