from playwright.sync_api import Locator, Page


class AddAccountDialog:
	def __init__(self, page: Page):
		self.page = page
		self.dialog: Locator = page.get_by_test_id("add-account-dialog")
		self.name_input: Locator = page.get_by_test_id("account-form-name-input")
		self.checking_option: Locator = page.get_by_role("option", name="Checking")
		self.type_options: Locator = page.get_by_test_id("account-form-type-options")
		self.savings_option: Locator = self.type_options.get_by_text("Savings")
		self.initial_balance_input: Locator = page.get_by_role("spinbutton", name="0.00")
		self.accept_terms_checkbox: Locator = page.get_by_test_id(
			"account-form-accept-terms-checkbox"
		)
		self.save_button: Locator = page.get_by_test_id("save-account-form-btn")

	def fill_initial_balance(self, balance: str) -> None:
		self.initial_balance_input.fill(balance)

	def accept_terms(self) -> None:
		self.accept_terms_checkbox.check()

	def save(self) -> None:
		self.save_button.click()