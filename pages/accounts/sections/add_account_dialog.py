from playwright.sync_api import Locator, Page
from models.account import AccountType
from models.money import Money


class AddAccountDialog:
	def __init__(self, page: Page):
		self.page = page
		self.dialog: Locator = page.get_by_test_id("add-account-dialog")
		self.name_input: Locator = page.get_by_test_id("account-form-name-input")
		self.type_options: Locator = page.get_by_test_id("account-form-type-select")
		self.initial_balance_input: Locator = page.get_by_role("spinbutton", name="0.00")
		self.accept_terms_checkbox: Locator = page.get_by_test_id(
			"account-form-accept-terms-checkbox"
		)
		self.save_button: Locator = page.get_by_test_id("save-account-form-btn")

	def fill_initial_balance(self, balance: Money) -> None:
		self.initial_balance_input.fill(str(balance.value))

	def select_account_type(self, account_type: AccountType) -> None:
		self.type_options.click()
		self.page.get_by_role("option", name=account_type.value).click()

	def accept_terms(self) -> None:
		self.accept_terms_checkbox.check()

	def save(self) -> None:
		self.save_button.click()