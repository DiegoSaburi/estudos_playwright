from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.todo.sections.filters import TodoFiltersSection
from pages.todo.sections.new_todo import NewTodoSection
from pages.todo.sections.todo_list import TodoListSection


class TodoPage(BasePage):
    PATH = "/todomvc/#/"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.new_todo = NewTodoSection(page)
        self.todo_list = TodoListSection(page)
        self.filters = TodoFiltersSection(page)

    def add_todo(self, text: str) -> None:
        self.new_todo.fill(text)
        self.new_todo.submit()

    def complete_todo(self, text: str) -> None:
        self.todo_list.toggle(text)

    def complete_todos(self, texts: list[str]) -> None:
        self.todo_list.toggle_many(texts)

    def show_active(self) -> None:
        self.filters.show_active()

    def open_todomvc(self) -> None:
        self.filters.open_todomvc()

    def get_body_text(self) -> str:
        return self.page.locator("body").inner_text()
