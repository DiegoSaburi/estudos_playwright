from playwright.sync_api import expect

from pages.qa_playground.page import PlaygroundFormPage
from pages.todo.page import TodoPage


def test_todo_app_tracks_tasks(todo_page: TodoPage):
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

    todo_page.complete_todos(["89", "0", "8", "7", "6", "5", "4", "3", "2", "uma task"])

    todo_page.show_active()
    assert "0 items left" in todo_page.get_body_text()
    todo_page.open_todomvc()


def test_complete_qa_playground_form(qa_playground_form_page: PlaygroundFormPage):
    qa_playground_form_page.login.fill("walter.white@gmail.com", "heisenberg")
    qa_playground_form_page.login.submit.click()
    expect(qa_playground_form_page.login.result).to_contain_text("Login successful! Welcome, walter.white@gmail.com.")

    qa_playground_form_page.personal.fill(
        first_name="Walter",
        last_name="White",
        phone="5551234567",
        dob="1958-09-07",
    )
    qa_playground_form_page.personal.male.check()
    qa_playground_form_page.personal.submit.click()
    expect(qa_playground_form_page.personal.result).to_contain_text("Saved: Walter White")

    qa_playground_form_page.address.fill(
        country="US",
        city="Albuquerque",
        about_you="Chemistry teacher turned meth kingpin. I am the one who knocks.",
    )
    qa_playground_form_page.address.submit.click()
    expect(qa_playground_form_page.address.result).to_contain_text("Address saved: Albuquerque, United States")

    qa_playground_form_page.interests.selenium.check()
    qa_playground_form_page.interests.playwright.check()
    qa_playground_form_page.interests.cypress.check()
    qa_playground_form_page.interests.appium.check()
    qa_playground_form_page.interests.submit.click()
    expect(qa_playground_form_page.interests.result).to_contain_text("Interests saved: Selenium, Playwright, Cypress, Appium")

    qa_playground_form_page.account.fill(
        password="saymyname",
        confirm_password="saymyname",
    )
    qa_playground_form_page.account.terms.check()
    qa_playground_form_page.account.submit.click()
    expect(qa_playground_form_page.account.success_message).to_be_visible()
    expect(qa_playground_form_page.account.success_message).to_contain_text("Account Setup Complete!")
