from playwright.sync_api import Page


class InterestsForm:
    def __init__(self, page: Page):
        self.selenium = page.get_by_test_id("checkbox-interest-selenium")
        self.playwright = page.get_by_test_id("checkbox-interest-playwright")
        self.cypress = page.get_by_test_id("checkbox-interest-cypress")
        self.appium = page.get_by_test_id("checkbox-interest-appium")
        self.jest = page.get_by_test_id("checkbox-interest-jest")
        self.submit = page.get_by_test_id("btn-interests-submit")

    def select_interests(self, interests: list[str] | None = None) -> None:
        interests = interests or []
        interest_map = {
            "selenium": self.selenium,
            "playwright": self.playwright,
            "cypress": self.cypress,
            "appium": self.appium,
            "jest": self.jest,
        }

        for interest in interests:
            key = interest.lower()
            if key in interest_map:
                interest_map[key].check()
