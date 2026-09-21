from playwright.sync_api import Locator, Page

from models.money import Money
from pages.accounts.sections.add_account_dialog import AddAccountDialog
from pages.base_page import BasePage


class AccountsPage(BasePage):
	PATH = "/bank/accounts"

	def __init__(self, page: Page, base_url: str):
		super().__init__(page, base_url)
		self.add_account_dialog = AddAccountDialog(page)
		self.account_row_balance: Locator = page.get_by_test_id("account-row-balance")
		self.account_page: Locator = page.get_by_test_id("accounts-page")
		self.add_account_button: Locator = page.get_by_test_id("add-account-btn")

	def get_total_balance(self) -> Money:
		total = Money.zero()
		for balance in self.account_row_balance.all():
			total += Money.from_text(balance.inner_text())
		return total