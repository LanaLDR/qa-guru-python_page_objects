import os

from selene import browser, have, command

from part1.data.users import User


class StudentRegistrationPage:

    def __init__(self):
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")

    def set_first_name(self, first_name):
        browser.element("#firstName").set_value(first_name)

    def set_last_name(self, last_name):
        browser.element("#lastName").set_value(last_name)

    def set_email(self, email):
        browser.element("#userEmail").set_value(email)

    def choose_gender(self, gender):
        browser.all("[name='gender']").element_by(have.value(gender)).element(
            ".."
        ).element("label").click()

    def set_mobile_number(self, number):
        browser.element("#userNumber").set_value(number)

    def choose_birth_date(self, birth_date):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").element(
            f'[value="{birth_date['year']}"]'
        ).click()
        browser.element(".react-datepicker__month-select").all("option").element_by(
            have.text(birth_date["month"])
        ).click()
        browser.element(f'.react-datepicker__day--0{birth_date["day"]}').click()

    def set_subjects(self, subjects):
        for subj in subjects:
            browser.element("#subjectsInput").set_value(subj).press_enter()

    def choose_hobbies(self, hobbies):
        for hobby in hobbies:
            browser.all("label[for^='hobbies']").element_by(have.text(hobby)).click()

    def upload_picture(self, image_name):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(f"tmp/{image_name}")
        )

    def set_address(self, address):
        browser.element("#currentAddress").set_value(address)

    def choose_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all("[id^='react-select']").element_by(have.text(state)).click()

    def choose_city(self, city):
        self.city.perform(command.js.scroll_into_view)
        self.city.click()
        browser.all("[id^='react-select']").element_by(have.text(city)).click()

    def submit_form(self):
        browser.element("#submit").submit()

    def register(self, user: User):
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.choose_gender(user.gender)
        self.set_mobile_number(user.number)
        self.choose_birth_date(user.birth_date)
        self.set_subjects(user.subjects)
        self.choose_hobbies(user.hobbies)
        self.upload_picture(user.image_name)
        self.set_address(user.address)
        self.choose_state(user.state)
        self.choose_city(user.city)
        self.submit_form()

    def should_registered_user_with(self, user: User):
        browser.element(".table-responsive").all("td").should(
            have.texts(
                "Student Name",
                f"{user.first_name} {user.last_name}",
                "Student Email",
                user.email,
                "Gender",
                user.gender,
                "Mobile",
                user.number,
                "Date of Birth",
                f"{user.birth_date['day']} {user.birth_date['month']},{user.birth_date['year']}",
                "Subjects",
                ", ".join(user.subjects),
                "Hobbies",
                ", ".join(user.hobbies),
                "Picture",
                user.image_name,
                "Address",
                user.address,
                "State and City",
                f"{user.state} {user.city}",
            )
        )
