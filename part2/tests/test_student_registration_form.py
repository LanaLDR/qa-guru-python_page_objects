from part2.data import users
from part2.pages.student_registration_page import StudentRegistrationPage


def test_success_filling_form(setup_browser):
    student_registration_page = StudentRegistrationPage()
    student = users.student

    student_registration_page.open()

    student_registration_page.register(student)
    student_registration_page.should_registered_user_with(student)
