from playwright.sync_api import sync_playwright

# Ask user for input

def info_park_jobs(search_keyword):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://infopark.in/companies/job-search")

        # Fill search box with user input
        page.locator("#job-search").fill(search_keyword)
        page.click("button >> .fa-magnifying-glass")
        page.wait_for_timeout(3000)

        print(f"{'Company Name':30} | {'Job Title':40} | {'Detail Link'}")
        print("-" * 100)

        while True:
            rows = page.locator("table tbody tr")
            count = rows.count()

            for i in range(count):
                job_title = rows.nth(i).locator("td:nth-child(2)").inner_text()
                company = rows.nth(i).locator("td:nth-child(3)").inner_text()
                detail_link = rows.nth(i).locator("td:nth-child(5) a").get_attribute("href")

                # Filter by user input keyword
                if search_keyword.upper() in job_title.upper():
                    if detail_link and not detail_link.startswith("http"):
                        detail_link = f"https://infopark.in{detail_link}"
                    print(f"{company:30} | {job_title:40} | {detail_link}")

            # Pagination
            next_button = page.locator("ul.pagination li a", has_text="Next")
            if next_button.count() == 0 or "disabled" in (next_button.get_attribute("class") or ""):
                break
            next_button.click()
            page.wait_for_timeout(2000)

        browser.close()
