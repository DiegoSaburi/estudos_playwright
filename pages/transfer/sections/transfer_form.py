from playwright.sync_api import Locator, Page

from models.account import Account
from models.money import Money
from models.transfer import Transfer, TransferDate


class TransferFormSection:
	def __init__(self, page: Page):
		self.page = page
		self.transfer_from_select: Locator = page.get_by_test_id("transfer-from-select")
		self.transfer_to_select: Locator = page.get_by_test_id("transfer-to-select")
		self.amount_input: Locator = page.get_by_test_id("transfer-amount-input")
		self.memo_input: Locator = page.get_by_role(
			"textbox", name="e.g. Rent, vacation fund…"
		)
		self.review_button: Locator = page.get_by_test_id("review-transfer-btn")

	def fill_transfer(self, transfer: Transfer) -> None:
		self.select_source_account(transfer.from_account)
		self.select_destination_account(transfer.to_account)
		self.fill_amount(transfer.amount)
		self.select_transfer_date(transfer.transfer_date)

	def select_source_account(self, account: Account) -> None:
		self.transfer_from_select.click()
		self.page.get_by_role("option", name=account.name).click()

	def select_destination_account(self, account: Account) -> None:
		self.transfer_to_select.click()
		self.page.get_by_role("option", name=account.name).click()

	def fill_amount(self, amount: Money) -> None:
		self.amount_input.fill(str(amount.value))

	def fill_memo(self, memo: str) -> None:
		self.memo_input.fill(memo)

	def select_transfer_date(self, transfer_date: TransferDate) -> None:
		self.page.get_by_role("radio", name=transfer_date.value).check()

	def review(self) -> None:
		self.review_button.click()