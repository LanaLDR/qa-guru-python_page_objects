from part1.data.users import student
from part1.pages.student_registration_page import StudentRegistrationPage


def test_success_filling_form(setup_browser):
    student_registration_page = StudentRegistrationPage()
    student_registration_page.open()

    student_registration_page.set_first_name(student.first_name)
    student_registration_page.set_last_name(student.last_name)
    student_registration_page.set_email(student.email)
    student_registration_page.choose_gender(student.gender)
    student_registration_page.set_mobile_number(student.number)
    student_registration_page.choose_birth_date(student.birth_date)
    student_registration_page.set_subjects(student.subjects)
    student_registration_page.choose_hobbies(student.hobbies)
    student_registration_page.upload_picture(student.image_name)
    student_registration_page.set_address(student.address)
    student_registration_page.choose_state(student.state)
    student_registration_page.choose_city(student.city)
    student_registration_page.submit_form()

    student_registration_page.should_registered_user_with(student)
