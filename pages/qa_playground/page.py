from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.qa_playground.sections.account_setup import AccountSetupForm
from pages.qa_playground.sections.address import AddressForm
from pages.qa_playground.sections.interests import InterestsForm
from pages.qa_playground.sections.login import LoginForm
from pages.qa_playground.sections.personal_info import PersonalDetailsForm


class PlaygroundFormPage(BasePage):
    PATH = "/practice/forms"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.login = LoginForm(page)
        self.personal = PersonalDetailsForm(page)
        self.address = AddressForm(page)
        self.interests = InterestsForm(page)
        self.account = AccountSetupForm(page)
