📘 Playwright All‑in‑One README (Python Sync API)
🔹 Core Concepts
Browser → Launch Chromium, Firefox, or WebKit.

Context → Isolated browser session (cookies, storage, viewport, locale).

Page → Represents a single tab where actions happen.

Locators → Handles to find and interact with elements. Lazy, auto‑waiting, chainable.

🔹 Selector Types
Role Selectors → Based on ARIA roles (button, checkbox, radio, link, textbox). Filter by name.

Label Selectors → Match inputs linked to <label>.

Placeholder Selectors → Match input fields by placeholder text.

Text Selectors → Match visible text content.

Alt Text Selectors → Match images by alt.

Title Selectors → Match elements by title.

Test ID Selectors → Match data-testid attributes (stable automation hooks).

CSS/XPath → Powerful but less stable; use for complex DOM structures.

🔹 Locator Features
Chaining → Refine locators step by step.

Filtering → Use .nth(), .first, .last.

Assertions → Check visibility, state, values.

Actions → click, fill, check, hover, press.

🔹 Common Actions
Form Inputs → Fill text, check/uncheck boxes, select options.

Clicks → Normal, double, right‑click, with position or modifiers.

Keyboard → Press keys, type text, insert text.

Mouse → Click, hover, drag & drop.

🔹 Navigation
goto, reload, go_back, go_forward.

🔹 Waiting
Timeouts → Hard wait with wait_for_timeout.

Element Waits → wait_for_selector, wait_for_load_state.

Event Waits → expect_popup, expect_download, expect_request.

🔹 Assertions
State → is_checked, is_visible, is_enabled.

Values → input_value, text_content.

Navigation → url, title.

🔹 Dialogs
Handle alerts, confirms, prompts with accept() or dismiss().

🔹 File Handling
Upload → Attach files with set_input_files.

Download → Capture with expect_download and save.

🔹 Frames & Popups
Frames → Access nested frames with page.frame(name="...").

Popups → Capture new tabs/windows with expect_popup.

🔹 Advanced Tools
Screenshots → Capture page or element.

Tracing → Record execution for debugging.

Video Recording → Enable in context for playback.

Network Control → Intercept requests, mock responses.

Storage State → Save/load cookies and local storage.

🔹 Best Practices
Prefer role/label/test‑id selectors → stable and readable.

Avoid brittle CSS/XPath unless necessary.

Use semantic attributes (ARIA roles, labels).

Chain locators for nested elements.

Use explicit waits instead of arbitrary timeouts.

Keep tests atomic (one scenario per test).

Always clean up with page.close(), context.close(), browser.close().

| Selector Type | Example | Best Use Case | Stability |
| --- | --- | --- | --- |
| Role | ``get_by_role("button")`` | Buttons, links, checkboxes | High |
| Label | ``get_by_label("Email")`` | Form inputs tied to labels | High |
| Placeholder | ``get_by_placeholder("Search")`` | Search boxes, text inputs | Medium |
| Text | ``get_by_text("Submit")`` | Buttons, headings, visible text | Medium |
| Alt Text | ``get_by_alt_text("Logo")`` | Images with alt attributes | High |
| Title | ``get_by_title("Close")`` | Elements with tooltip/title | Medium |
| Test ID | ``get_by_test_id("id")`` | Stable automation hooks | Very High |
| CSS/XPath | ``locator("css=div ``> ``p")`` | Complex DOM, fallback | Low–Medium |

🔹 Typical Workflow
Launch browser → create context → open page.

Navigate to site.

Perform actions (login, form fill, clicks).

Validate with assertions.

Handle dialogs, downloads, frames if needed.

Close everything cleanly.