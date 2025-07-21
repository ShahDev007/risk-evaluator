# File: ui_tests/test_dashboard.py
import time
from selenium.webdriver.common.by import By


def test_dashboard_loads(browser):
    browser.get("http://localhost:5173/dashboard")
    time.sleep(1)  # wait for table to load (you can replace with WebDriverWait)

    heading = browser.find_element(By.TAG_NAME, "h2")
    assert heading.text == "Loan Cases"

    rows = browser.find_elements(By.CSS_SELECTOR, "table tbody tr")
    assert len(rows) == 2

    # Validate first row content
    assert "John Doe" in rows[0].text
    assert "712" in rows[0].text


def test_case_navigation(browser):
    browser.get("http://localhost:5173/dashboard")
    time.sleep(1)

    # Click the first "View" button
    view_btn = browser.find_element(By.CSS_SELECTOR, "a.btn.btn-secondary")
    view_btn.click()

    time.sleep(1)
    assert "/case/1" in browser.current_url
    assert "Case Details for ID: 1" in browser.page_source
