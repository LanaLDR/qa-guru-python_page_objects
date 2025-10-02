from selene import browser

from part3.model.components.panel import Panel
from part3.model.pages.simple_user_registration_page import SimpleUserRegistrationPage
from part3.model.pages.student_registration_page import StudentRegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleUserRegistrationPage()
        self.panel = Panel()
        self.student_registration_page = StudentRegistrationPage()


app = Application()
