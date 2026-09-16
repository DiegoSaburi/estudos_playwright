from playwright.sync_api import Page


class AddressForm:
    def __init__(self, page: Page):
        self.country = page.get_by_test_id("select-country")
        self.city = page.get_by_test_id("input-city")
        self.about = page.get_by_role("textbox", name="About You optional · no testid")
        self.submit = page.get_by_test_id("btn-address-submit")
        self.result = page.get_by_test_id("result-address")

    def fill(self, country: str = "", city: str = "", about_you: str = "") -> None:
        self.country.select_option(country)
        self.city.fill(city)
        self.about.fill(about_you)
