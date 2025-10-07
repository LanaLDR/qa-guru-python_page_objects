from part1.pages.student_registration_page import StudentRegistrationPage


def test_success_filling_form(setup_browser):
    student_registration_page = StudentRegistrationPage()
    student_registration_page.open()

    student_registration_page.set_first_name("Kirill")
    student_registration_page.set_last_name("Semin")
    student_registration_page.set_email("testemail1324@gmail.com")
    student_registration_page.choose_gender("Male")
    student_registration_page.set_mobile_number("9803628839")
    student_registration_page.choose_birth_date(
        {"day": 20, "month": "January", "year": 1999}
    )
    student_registration_page.set_subjects(
        ["Maths", "English", "Physics", "Chemistry", "Computer Science"]
    )
    student_registration_page.choose_hobbies(["Sports", "Reading"])
    student_registration_page.upload_picture("cat.jpg")
    student_registration_page.set_address("Emlutina 13")
    student_registration_page.choose_state("NCR")
    student_registration_page.choose_city("Delhi")
    student_registration_page.submit_form()

    student_registration_page.should_registered_user_with(
        "Kirill",
        "Semin",
        "testemail1324@gmail.com",
        "Male",
        "9803628839",
        {"day": 20, "month": "January", "year": 1999},
        ["Maths", "English", "Physics", "Chemistry", "Computer Science"],
        ["Sports", "Reading"],
        "cat.jpg",
        "NCR",
        "Delhi",
        "Emlutina 13",
    )
