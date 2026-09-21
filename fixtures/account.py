from collections.abc import Callable

import pytest
from playwright.sync_api import expect

from models.account import Account
from pages.accounts.page import AccountsPage
from pages.sidebar.page import SidebarPage


@pytest.fixture
def create_account(
    accounts_page: AccountsPage,
    sidebar_page: SidebarPage,
) -> Callable[[Account], Account]:
    def _create_account(account: Account) -> Account:
        sidebar_page.accounts.click()
        expect(accounts_page.account_page).to_be_visible()

        accounts_page.add_account_button.click()
        expect(accounts_page.add_account_dialog.dialog).to_be_visible()

        accounts_page.add_account_dialog.add_account(account)

        expect(accounts_page.add_account_dialog.dialog).not_to_be_visible()
        return account

    return _create_account