"# playwright"



pip install playwright

playwright install


📘 Playwright All‑in‑One README (Python Sync API)
🔹 Core Concepts
Browser → Launch Chromium, Firefox, or WebKit.

Context → Isolated browser session (cookies, storage, viewport, locale).

Page → Represents a single tab where actions happen.

Selectors → Identify elements (get_by_label, get_by_role, locator, CSS, XPath).

🔹 Selector Types (Deep Dive)
Role Selectors → Based on ARIA roles (button, checkbox, radio, link, textbox). Use name for visible text.

Label Selectors → Match inputs linked to <label>.

Placeholder Selectors → Match by placeholder text.

Text Selectors → Match visible text content.

Alt Text Selectors → Match images by alt.

Title Selectors → Match elements by title.

Test ID Selectors → Match data-testid attributes (stable automation hooks).

CSS/XPath → Powerful but less stable; use for complex DOM structures.

🔹 Common Actions
Form Inputs → fill, check, uncheck, select_option.

Clicks → click, with options for position, modifiers, force.

Keyboard → press, type, insert_text.

Mouse → click, dblclick, hover, drag_to.

🔹 Navigation
goto, reload, go_back, go_forward.

🔹 Waiting
Timeouts → wait_for_timeout(ms) (hard wait).

Element Waits → wait_for_selector, wait_for_load_state.

Event Waits → expect_popup, expect_download, expect_request.

🔹 Assertions
State → is_checked, is_visible, is_enabled.

Values → input_value, text_content.

Navigation → url, title.

🔹 Dialogs
Handle alerts, confirms, prompts with dialog.accept() or dialog.dismiss().

🔹 File Handling
Upload → set_input_files.

Download → expect_download → save_as.

🔹 Frames & Popups
Frames → Access with page.frame(name="...").

Popups → Capture new tabs/windows with expect_popup.

🔹 Advanced Tools
Screenshots → Capture page or element.

Tracing → Record execution for debugging.

Video Recording → Enable in context for playback.

Network Control → Intercept requests, mock responses.

Storage State → Save/load cookies and local storage.

🔹 Best Practices
Prefer role/label/test‑id selectors over CSS/XPath.

Use explicit waits instead of arbitrary timeouts.

Keep tests atomic (one scenario per test).

Use contexts to isolate sessions.

Always clean up with page.close(), context.close(), browser.close().

🔹 Typical Workflow
Launch browser → create context → open page.

Navigate to site.

Perform actions (login, form fill, clicks).

Validate with assertions.

Handle dialogs, downloads, frames if needed.

Close everything cleanly.
