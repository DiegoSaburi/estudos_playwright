from playwright.sync_api import Locator, Page


class RecentTransactionsSection:
	def __init__(self, page: Page):
		self.page = page
		self.section: Locator = page.get_by_test_id("recent-transactions-section")
