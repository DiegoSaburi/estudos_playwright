import re

from playwright.sync_api import Page, expect

from conftest import dashboard_page
from models.user import User
from pages import sidebar
from pages.accounts.page import AccountsPage
from pages.dashboard.page import DashboardPage
from pages.sidebar.page import SidebarPage


def test_standard_user_can_see_dashboard(
	standard_user: User,
	dashboard_page: DashboardPage,
	page: Page,
):
	expect(page).to_have_url(re.compile(r".*/bank/dashboard"))
	expect(dashboard_page.overview.total_net_worth).to_be_visible()
	expect(dashboard_page.overview.net_change).to_be_visible()
	expect(dashboard_page.overview.income).to_be_visible()
	expect(dashboard_page.overview.expenses).to_be_visible()
	
	expect(dashboard_page.quick_actions.transfer).to_be_visible()
	expect(dashboard_page.quick_actions.bill_pay).to_be_visible()
	expect(dashboard_page.quick_actions.apply_loan).to_be_visible()
	expect(dashboard_page.quick_actions.transactions).to_be_visible()
	
	expect(dashboard_page.recent_transactions.section).to_be_visible()

def test_verify_total_balance_display(
    standard_user: User,
    dashboard_page: DashboardPage,
    sidebar_page: SidebarPage,
    accounts_page: AccountsPage,
    page: Page,
):
    sidebar_page.accounts.click()
    expect(page).to_have_url(re.compile(r".*/bank/accounts"))
    accounts_total_balance = accounts_page.get_total_balance()

    sidebar_page.dashboard.click()
    expect(page).to_have_url(re.compile(r".*/bank/dashboard"))

    dashboard_total_balance = dashboard_page.overview.get_total_net_worth()
    assert accounts_total_balance == dashboard_total_balance