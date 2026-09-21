from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.dashboard.sections.overview import OverviewSection
from pages.dashboard.sections.quick_actions import QuickActionsSection
from pages.dashboard.sections.recent_transactions import RecentTransactionsSection
from pages.sidebar.page import SidebarPage


class DashboardPage(BasePage):
	PATH = "/bank/"

	def __init__(self, page: Page, base_url: str):
		super().__init__(page, base_url)
		self.overview = OverviewSection(page)
		self.quick_actions = QuickActionsSection(page)
		self.recent_transactions = RecentTransactionsSection(page)
		self.sidebar = SidebarPage(page)
