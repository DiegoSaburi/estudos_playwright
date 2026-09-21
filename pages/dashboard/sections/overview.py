from playwright.sync_api import Locator, Page

from models.money import Money


class OverviewSection:
	def __init__(self, page: Page):
		self.page = page
		self.total_net_worth: Locator = page.get_by_test_id("stat-card-net-worth-value")
		self.net_change: Locator = page.get_by_test_id("stat-card-value")
		self.income: Locator = page.get_by_label("Monthly income amount")
		self.expenses: Locator = page.get_by_test_id("dashboard-stat-cards")

	def get_total_net_worth(self) -> Money:
		return Money.from_text(self.total_net_worth.inner_text())

	def get_net_change(self) -> Money:
		return Money.from_text(self.net_change.inner_text())

	def get_income(self) -> Money:
		return Money.from_text(self.income.inner_text())

	def get_expenses(self) -> Money:
		return Money.from_text(self.expenses.inner_text())
