from playwright.sync_api import Page

from pages.qa_playground.sections.account_setup import AccountSetupForm
from pages.qa_playground.sections.address import AddressForm
from pages.qa_playground.sections.interests import InterestsForm
from pages.qa_playground.sections.login import LoginForm
from pages.qa_playground.sections.personal_info import PersonalDetailsForm


class PlaygroundFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.login = LoginForm(page)
        self.personal = PersonalDetailsForm(page)
        self.address = AddressForm(page)
        self.interests = InterestsForm(page)
        self.account = AccountSetupForm(page)
