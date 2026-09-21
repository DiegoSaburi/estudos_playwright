from playwright.sync_api import Locator, Page


class QuickActionsSection:
	def __init__(self, page: Page):
		self.page = page
		self.section: Locator = page.get_by_test_id("quick-actions-section")
		self.transfer: Locator = page.get_by_test_id("quick-action-transfer")
		self.bill_pay: Locator = page.get_by_test_id("quick-action-bill-pay")
		self.apply_loan: Locator = page.get_by_test_id("quick-action-apply-loan")
		self.transactions: Locator = page.get_by_test_id("quick-action-transactions")
