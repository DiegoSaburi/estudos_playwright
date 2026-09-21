import re

from playwright.sync_api import expect

from models.account import Account, AccountType
from models.money import Money
from models.user import User
from pages.accounts.page import AccountsPage
from pages.sidebar.page import SidebarPage
from data.account_factory import AccountFactory


def test_verify_accounts_list_load(
    standard_user: User,
    accounts_page: AccountsPage,
    sidebar_page: SidebarPage,
):
    sidebar_page.accounts.click()

    expect(accounts_page.page).to_have_url(re.compile(r".*/bank/accounts"))
    expect(accounts_page.account_page).to_be_visible()
    expect(accounts_page.account_row_balance.first).to_be_visible()


def test_create_account(
    standard_user: User,
    accounts_page: AccountsPage,
    sidebar_page: SidebarPage,
):
    account = AccountFactory().create()

    sidebar_page.accounts.click()
    expect(accounts_page.account_page).to_be_visible()
    expect(accounts_page.page).to_have_url(re.compile(r".*/bank/accounts"))

    accounts_page.add_account_button.click()
    expect(accounts_page.add_account_dialog.dialog).to_be_visible()

    accounts_page.add_account_dialog.name_input.fill(account.name)
    accounts_page.add_account_dialog.select_account_type(account.type)
    accounts_page.add_account_dialog.fill_initial_balance(account.starting_balance)
    accounts_page.add_account_dialog.accept_terms()
    accounts_page.add_account_dialog.save()

    expect(accounts_page.add_account_dialog.dialog).not_to_be_visible()
    expect(accounts_page.page.get_by_text(account.name, exact=True)).to_be_visible()
    expect(accounts_page.page.get_by_text(str(account.starting_balance), exact=True)).to_be_visible()
