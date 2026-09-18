from playwright.sync_api import Page


class LoginForm:
    def __init__(self, page: Page):
        self.email = page.get_by_test_id("input-login-email")
        self.password = page.get_by_test_id("form-login-inner").get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_test_id("btn-login-submit")
        self.result = page.get_by_test_id("result-login")

    def fill(self, email: str = "", password: str = "") -> None:
        self.email.fill(email)
        self.password.fill(password)

    def submit(self) -> None:
        self.submit_button.click()
