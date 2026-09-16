from playwright.sync_api import Page


class TodoFiltersSection:
    def __init__(self, page: Page):
        self.page = page

    def show_active(self) -> None:
        self.page.get_by_role("link", name="Active").click()

    def show_completed(self) -> None:
        self.page.get_by_role("link", name="Completed").click()

    def open_todomvc(self) -> None:
        self.page.get_by_role("link", name="real TodoMVC app.").click()
