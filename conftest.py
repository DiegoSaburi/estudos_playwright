from collections.abc import Callable

import pytest
from playwright.sync_api import Page

from config.loader import Config
from data.users import (
    ADMIN_USER,
    ERROR_USER,
    FROZEN_USER,
    LOCKED_USER,
    OVERDRAFT_USER,
    SLOW_USER,
    STANDARD_USER,
)
from fixtures.account import create_account
from models.user import User
from pages.sidebar.page import SidebarPage
from pages.accounts.page import AccountsPage
from pages.bank.page import BankPage
from pages.dashboard.page import DashboardPage
from pages.login.page import LoginPage
from pages.qa_playground.page import PlaygroundFormPage
from pages.todo.page import TodoPage
from pages.transfer.page import TransferPage


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa1",
        choices=["qa1", "qa2", "stg"],
    )


@pytest.fixture(scope="session")
def config(request) -> Config:
    return Config(request.config.getoption("--env"))


@pytest.fixture(autouse=True)
def configure_page(page: Page, config: Config) -> None:
    page.set_default_timeout(config.default_timeout)
    page.set_default_navigation_timeout(config.navigation_timeout)


@pytest.fixture
def todo_page(page: Page, config: Config) -> TodoPage:
    todo = TodoPage(page, config.todo_base_url)
    todo.open()
    return todo


@pytest.fixture
def playwright_page(page: Page, config: Config) -> Page:
    page.goto(config.playwright_base_url)
    return page


@pytest.fixture
def qa_playground_form_page(page: Page, config: Config) -> PlaygroundFormPage:
    form = PlaygroundFormPage(page, config.web_base_url)
    form.open()
    return form


@pytest.fixture
def login_page(page: Page, config: Config) -> LoginPage:
    login = LoginPage(page, config.web_base_url)
    login.open()
    return login


@pytest.fixture
def secure_bank_page(login_page: LoginPage) -> LoginPage:
    return login_page


@pytest.fixture
def bank_page(page: Page, config: Config) -> BankPage:
    bank = BankPage(page, config.web_base_url)
    bank.open()
    return bank


@pytest.fixture
def dashboard_page(page: Page, config: Config) -> DashboardPage:
    return DashboardPage(page, config.web_base_url)


@pytest.fixture
def accounts_page(page: Page, config: Config) -> AccountsPage:
    return AccountsPage(page, config.web_base_url)


@pytest.fixture
def transfer_page(page: Page, config: Config) -> TransferPage:
    transfer = TransferPage(page, config.web_base_url)
    transfer.open()
    return transfer

@pytest.fixture
def sidebar_page(page: Page) -> SidebarPage:
    return SidebarPage(page)

@pytest.fixture
def login_as(login_page: LoginPage) -> Callable[[User], User]:
    def _login_as(user: User) -> User:
        login_page.login(user.username, user.password)
        return user

    return _login_as


@pytest.fixture
def standard_user(login_as) -> User:
    return login_as(STANDARD_USER)


@pytest.fixture
def locked_user(login_as) -> User:
    return login_as(LOCKED_USER)


@pytest.fixture
def frozen_user(login_as) -> User:
    return login_as(FROZEN_USER)


@pytest.fixture
def overdraft_user(login_as) -> User:
    return login_as(OVERDRAFT_USER)


@pytest.fixture
def slow_user(login_as) -> User:
    return login_as(SLOW_USER)


@pytest.fixture
def error_user(login_as) -> User:
    return login_as(ERROR_USER)


@pytest.fixture
def admin_user(login_as) -> User:
    return login_as(ADMIN_USER)