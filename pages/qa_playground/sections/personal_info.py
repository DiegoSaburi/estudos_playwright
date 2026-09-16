from playwright.sync_api import Page


class PersonalDetailsForm:
    def __init__(self, page: Page):
        self.first_name = page.get_by_test_id("input-first-name")
        self.last_name = page.get_by_test_id("input-last-name")
        self.phone = page.get_by_test_id("input-phone")
        self.dob = page.get_by_test_id("input-dob")
        self.male = page.get_by_test_id("radio-gender-male")
        self.female = page.get_by_test_id("radio-gender-female")
        self.other = page.get_by_test_id("radio-gender-other")
        self.submit = page.get_by_test_id("btn-personal-submit")
        self.result = page.get_by_test_id("result-personal")

    def fill(self, first_name: str = "", last_name: str = "", phone: str = "", dob: str = "") -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.phone.fill(phone)
        self.dob.fill(dob)
