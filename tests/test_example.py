import re
from playwright.sync_api import Page, expect

from pages.qa_playground.page import PlaygroundFormPage
from pages.todo.page import TodoPage


def test_has_title(playwright_page: Page):
    expect(playwright_page).to_have_title(re.compile("Playwright"))


def test_get_started_link(playwright_page: Page):
    playwright_page.get_by_role("link", name="Get started").click()
    expect(playwright_page.get_by_role("heading", name="Installation")).to_be_visible()


def test_playright_mvc(todo_page: TodoPage):
    todo_page.add_todo("uma task")
    todo_page.add_todo("2")
    todo_page.add_todo("3")
    todo_page.add_todo("4")
    todo_page.add_todo("5")
    todo_page.add_todo("6")
    todo_page.add_todo("7")
    todo_page.add_todo("8")
    todo_page.add_todo("89")
    todo_page.add_todo("0")

    todo_page.page.locator("li:nth-child(9) > .view > .toggle").check()
    todo_page.page.locator("li:nth-child(10) > .view > .toggle").check()
    todo_page.page.locator("li:nth-child(8) > .view > .toggle").check()
    todo_page.page.locator("li:nth-child(7) > .view > .toggle").check()
    todo_page.page.get_by_role("listitem").filter(has_text="6").get_by_label("Toggle Todo").check()
    todo_page.page.get_by_role("listitem").filter(has_text="5").get_by_label("Toggle Todo").check()
    todo_page.page.get_by_role("listitem").filter(has_text="4").get_by_label("Toggle Todo").check()
    todo_page.page.get_by_role("listitem").filter(has_text="3").get_by_label("Toggle Todo").check()
    todo_page.page.get_by_role("listitem").filter(has_text="2").get_by_label("Toggle Todo").check()
    todo_page.page.get_by_role("listitem").filter(has_text="uma task").get_by_label("Toggle Todo").check()

    todo_page.page.get_by_role("link", name="Active").click()
    expect(todo_page.page.locator("body")).to_contain_text("0 items left")
    todo_page.page.get_by_role("link", name="real TodoMVC app.").click()


def test_fill_form_successfully(qa_playground_form_page: PlaygroundFormPage):
    qa_playground_form_page.login.fill("walter.white@gmail.com", "heisenberg")
    qa_playground_form_page.login.submit.click()

    qa_playground_form_page.personal.fill(
        first_name="Walter",
        last_name="White",
        phone="5551234567",
        dob="1958-09-07",
        gender="male",
    )
    qa_playground_form_page.personal.submit.click()

    qa_playground_form_page.address.fill(
        country="US",
        city="Albuquerque",
        about_you="Chemistry teacher turned meth kingpin. I am the one who knocks.",
    )
    qa_playground_form_page.address.submit.click()

    qa_playground_form_page.interests.select_interests([
        "selenium",
        "playwright",
        "cypress",
        "appium",
    ])
    qa_playground_form_page.interests.submit.click()

    qa_playground_form_page.account.fill(
        password="saymyname",
        confirm_password="saymyname",
    )
    qa_playground_form_page.account.submit.click()
