def test_login_success(browser):
    browser.get("http://localhost:5173/login")

    email_input = browser.find_element("id", "email")
    password_input = browser.find_element("id", "password")
    login_button = browser.find_element("xpath", "//button[@type='submit']")

    email_input.send_keys("abc@gmail.com")
    password_input.send_keys("abc")
    login_button.click()

    assert "dashboard" in browser.current_url.lower()
