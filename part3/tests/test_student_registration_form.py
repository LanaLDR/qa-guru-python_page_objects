from part3.Application import app
from part3.data import users


def test_success_filling_form(setup_browser):
    student = users.student
    app.student_registration_page.open()

    app.student_registration_page.register(student)
    app.student_registration_page.should_registered_user_with(student)
