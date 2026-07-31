import asyncio
from playwright.async_api import async_playwright

"""| Locator Type | Where to Test on This Page |
| --- | --- |
| **ID / CSS ID** | “Simple Form Demo” → input fields have stable IDs |
| **CSS Class** | Buttons like ``.btn-primary`` |
| **CSS Attribute Selector** | ``input[type='text']`` in forms |
| **XPath by Text** | Links like ``//a[text()='Checkbox ``Demo']`` |
| **XPath by Attribute** | ``//input[@id='sum1']`` |
| **XPath Indexing** | Multiple checkboxes → ``(//input[@type='checkbox'])[3]`` |
| **XPath Contains (Attribute)** | Dynamic elements in “Dynamic ID” page |
| **XPath Contains (Text)** | Long text in “Table Pagination” page |
"""

#By ID -id-attr value
async def by_id():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})#type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("#username").fill("practice")
        await page.locator("#password").fill("SuperSecretPassword!")
        await page.locator("#submit-login").click()
        await page.wait_for_timeout(2000)

#By CSS selector -#idname,.class name
async def by_css_selector():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})#type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator(".form-control").nth(0).fill("practice")
        await page.locator(".form-control").nth(1).fill("SuperSecretPassword!")
        await page.locator(".btn-primary").click()
        await page.wait_for_timeout(2000)

# When the attribute value contains combination of character,
# special characters, and numbers, one should not use the attribute
# value to get the element as the id changes dynamically

async def by_css_attribute_selector():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})#type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("input[name='username']").fill("practice")
        await page.locator("input[name='password']").fill("SuperSecretPassword!")
        await page.locator("button[name='submit-login']").click()
        await page.wait_for_timeout(2000)

#Xpath
# 1. xpath by visible text -//tag name[text() = 'visible text']

async def xpath_by_visible_text():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})  # type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("//label[text()='Username']").fill("practice")
        await page.locator("//label[text()='Password']").fill("SuperSecretPassword!")
        await page.locator("//button[text()='Login']").click()
        await page.wait_for_timeout(2000)


#2. xpath by attribute -//tag name[@attr name = 'attr value']

async def xpath_by_attribute_selector():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})#type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("//input[@name='username']").fill("practice")
        await page.locator("//input[@name='password']").fill("SuperSecretPassword!")
        await page.locator("//button[@name='submit-login']").click()
        await page.wait_for_timeout(2000)

#3 . xpath by contains -Usage
# reason -When the attribute value is long or changes
# dynamically -//tag name[contains(@attr name,'partial Fixed attr value')]

async def xpath_by_xpath():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})  # type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("//label[contains(text(), 'Username')]").fill("practice")
        await page.locator("//input[contains(@name, 'password')]").fill("SuperSecretPassword!")
        await page.locator("//button[contains(text(), 'Login')]").click()
        await page.wait_for_timeout(2000)
#xpath by contains by visible text -Usage reason -When the text is long//tag name[contains(text(),'partial text')]

async def xpath_by_visible_text_partial():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page(viewport={'width': 800, 'height': 600})  # type: ignore
        await page.goto("https://practice.expandtesting.com/login")
        await page.locator("//label[contains(text(), 'Usern')]").fill("practice")
        await page.locator("//label[contains(text(), 'Passwo')]").fill("SuperSecretPassword!")
        await page.locator("//button[contains(text(), 'Login')]").click()
        await page.wait_for_timeout(2000)

if __name__ == '__main__':
    """
    asyncio.run(by_id())
    asyncio.run(by_css_selector()
    asyncio.run(by_css_attribute_selector())
    asyncio.run(xpath_by_visible_text())
    asyncio.run(xpath_by_visible_text())
    asyncio.run(xpath_by_xpath())
    """
    asyncio.run(xpath_by_visible_text_partial())


