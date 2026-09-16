from playwright.sync_api import Page


class InterestsForm:
    def __init__(self, page: Page):
        self.selenium = page.get_by_test_id("checkbox-interest-selenium")
        self.playwright = page.get_by_test_id("checkbox-interest-playwright")
        self.cypress = page.get_by_test_id("checkbox-interest-cypress")
        self.appium = page.get_by_test_id("checkbox-interest-appium")
        self.jest = page.get_by_test_id("checkbox-interest-jest")
        self.submit = page.get_by_test_id("btn-interests-submit")
        self.result = page.get_by_test_id("result-interests")
