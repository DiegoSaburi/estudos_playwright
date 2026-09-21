from playwright.sync_api import Locator, Page


class TransferConfirmationSection:
	def __init__(self, page: Page):
		self.page = page
		self.dialog: Locator = page.get_by_test_id("transfer-confirm-dialog")
		self.confirm_button: Locator = page.get_by_test_id("confirm-transfer-btn")
		self.confirmation_page: Locator = page.get_by_test_id("transfer-confirmation-page")
		self.success_heading: Locator = page.get_by_test_id("transfer-success-heading")

	def confirm(self) -> None:
		self.confirm_button.click()