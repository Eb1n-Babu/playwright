from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            locale='en-US',
            timezone_id="Asia/Shanghai"
        )
        page = await context.new_page()
        await page.goto("https://forms.gle/eLma4adqHN7RNLvT7")

        # Target only enabled textboxes (Google Forms disables the first dummy input)
        enabled_inputs = page.locator("input[type='text'][aria-disabled='false'], textarea[aria-disabled='false']")

        # Fill required fields
        await enabled_inputs.nth(0).fill("skmwsw swjs")             # Name
        await enabled_inputs.nth(1).fill("dckcmkcmkemxksw@example.com") # Email
        await enabled_inputs.nth(2).fill("Kerala, India")         # Address

        # Optional fields
        await enabled_inputs.nth(3).fill("+91 738030389")        # Phone number
        await enabled_inputs.nth(4).fill("Looking forward!")      # Comments

        # Submit the form
        await page.get_by_role("button", name="Submit").click()

        # Close everything
        await page.close()
        await context.close()
        await browser.close()

asyncio.run(main())
