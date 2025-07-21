from playwright.sync_api import sync_playwright

def run_playwright_demo():
    with sync_playwright() as p:
        # Create browser context with proper viewport
        browser = p.chromium.launch(headless=False)  # Make browser visible for debugging
        context = browser.new_context(viewport={"width": 1280, "height": 800})  # Spacious view
        page = context.new_page()

        # Navigate to site and wait for it to fully load
        response = page.goto("https://www.realmadrid.com/en-US")
        print("Response status:", response.status)

        page.wait_for_load_state("networkidle")  # Wait until page resources finish loading

        # Debug: check page content
        print("Loaded HTML snippet:", page.content()[:100])  # Just a sneak peek!

        # Capture screenshot after everything's ready
        page.screenshot(path=r"./screenshot.png")
        print("Screenshot captured successfully! 📸")

        browser.close()
if __name__ == "__main__":
    run_playwright_demo()