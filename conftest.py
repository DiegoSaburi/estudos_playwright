import pytest
from playwright.sync_api import Page

from pages.qa_playground.page import PlaygroundFormPage
from pages.todo.page import TodoPage


@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    return TodoPage(page)


@pytest.fixture
def playwright_page(page: Page) -> Page:
    page.goto("https://playwright.dev/")
    return page


@pytest.fixture
def qa_playground_form_page(page: Page) -> PlaygroundFormPage:
    page.goto("https://qaplayground.com/practice/forms")
    return PlaygroundFormPage(page)