from playwright.sync_api import Page


class AccountSetupForm:
    def __init__(self, page: Page):
        self.password = page.get_by_test_id("input-password")
        self.confirm = page.get_by_test_id("input-confirm-password")
        self.submit_button = page.get_by_test_id("submit-form-btn")
        self.terms = page.get_by_test_id("checkbox-terms")
        self.success_message = page.get_by_test_id("form-success-msg")

    def fill(self, password: str = "", confirm_password: str = "") -> None:
        self.password.fill(password)
        self.confirm.fill(confirm_password)

    def submit(self) -> None:
        self.submit_button.click()
