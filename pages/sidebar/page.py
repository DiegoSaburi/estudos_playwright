from playwright.sync_api import Locator, Page


class SidebarPage:
	def __init__(self, page: Page):
		self.page = page
		self.dashboard: Locator = page.get_by_test_id("sidebar-link-dashboard")
		self.accounts: Locator = page.get_by_test_id("sidebar-link-accounts")
		self.transfer: Locator = page.get_by_test_id("sidebar-link-transfer")
		self.send_money: Locator = page.get_by_test_id("sidebar-link-send-money")
		self.bill_pay: Locator = page.get_by_test_id("sidebar-link-bill-pay")
		self.transactions: Locator = page.get_by_test_id("sidebar-link-transactions")
		self.apply_loan: Locator = page.get_by_test_id("sidebar-link-apply-loan")
		self.notifications: Locator = page.get_by_test_id("sidebar-link-notifications")
		self.profile: Locator = page.get_by_test_id("sidebar-link-profile")
		self.user_info: Locator = page.get_by_test_id("sidebar-user-info")
