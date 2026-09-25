import re

from playwright.sync_api import expect

from models.account import AccountType, Account
from models.money import Money
from models.transfer import Transfer, TransferDate
from models.user import User
from pages.dashboard.page import DashboardPage
from pages.transfer.page import TransferPage


def test_verify_successful_internal_transfer(
	standard_user: User,
	create_account,
	dashboard_page: DashboardPage,
):
	source_account = Account(
		name="Automation Transfer Source",
		type=AccountType.CHECKING,
		starting_balance=Money.from_text("2000.00"),
	)
	
	destination_account = Account(
		name="Automation Transfer Destination",
		type=AccountType.SAVINGS,
		starting_balance=Money.from_text("2000.00"),
	)

	create_account(source_account)
	create_account(destination_account)
	
	dashboard_page.open()
	dashboard_page.quick_actions.transfer.click()
	transfer_page = TransferPage(dashboard_page.page, dashboard_page.base_url)
	expect(transfer_page.page).to_have_url(re.compile(r".*/bank/transfer"))

	transfer = Transfer(
		from_account=source_account,
		to_account=destination_account,
		amount=Money.from_text("1000.00"),
		transfer_date=TransferDate.TODAY,
	)
	transfer_page.fill_transfer(transfer)
	transfer_page.form.fill_memo("Internal transfer")
	transfer_page.form.review()

	expect(transfer_page.confirmation.dialog).to_be_visible()
	transfer_page.confirmation.confirm()
	expect(transfer_page.confirmation.confirmation_page).to_be_visible()
	expect(transfer_page.confirmation.success_heading).to_be_visible()


def test_verify_insufficient_funds_validation(
	standard_user: User,
	create_account,
	dashboard_page: DashboardPage,
):
	source_account = Account(
		name="Automation Insufficient Funds Source",
		type=AccountType.CHECKING,
		starting_balance=Money.from_text("500.00"),
	)
	destination_account = Account(
		name="Automation Insufficient Funds Destination",
		type=AccountType.SAVINGS,
		starting_balance=Money.from_text("2000.00"),
	)

	create_account(source_account)
	create_account(destination_account)
	
	dashboard_page.open()
	dashboard_page.quick_actions.transfer.click()
	transfer_page = TransferPage(dashboard_page.page, dashboard_page.base_url)
	expect(transfer_page.page).to_have_url(re.compile(r".*/bank/transfer"))

	transfer = Transfer(
		from_account=source_account,
		to_account=destination_account,
		amount=Money.from_text("1000.00"),
		transfer_date=TransferDate.TODAY,
	)
	transfer_page.fill_transfer(transfer)
	transfer_page.form.fill_memo("Insufficient funds transfer")
	transfer_page.form.review()

	expect(transfer_page.confirmation.dialog).to_be_visible()
	transfer_page.confirmation.confirm()

	expect(transfer_page.form.error_message).to_be_visible()
	expect(transfer_page.form.error_message).to_contain_text(f'Insufficient funds. Available balance: {str(source_account.starting_balance)}.')