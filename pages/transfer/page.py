from playwright.sync_api import Page

from models.transfer import Transfer
from pages.base_page import BasePage
from pages.transfer.sections.transfer_confirmation import TransferConfirmationSection
from pages.transfer.sections.transfer_form import TransferFormSection


class TransferPage(BasePage):
	PATH = "/bank/transfer"

	def __init__(self, page: Page, base_url: str):
		super().__init__(page, base_url)
		self.form = TransferFormSection(page)
		self.confirmation = TransferConfirmationSection(page)

	def fill_transfer(self, transfer: Transfer) -> None:
		self.form.fill_transfer(transfer)
