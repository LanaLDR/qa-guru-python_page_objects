from selene import browser, have, command

from part3.data.users import SimpleUser


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit_button = browser.element("#submit")
        self.output_user_info = browser.element("#output")

    def open(self):
        browser.open("/text-box")

    def fill_full_name(self, full_name):
        self.full_name.type(full_name)

    def fill_email(self, email):
        self.email.type(email)

    def fill_current_address(self, current_address):
        self.current_address.type(current_address)

    def fill_permanent_address(self, permanent_address):
        self.permanent_address.type(permanent_address)

    def submit(self):
        self.submit_button.perform(command.js.scroll_into_view).click()

    def should_have_submited(self, simple_user: SimpleUser):
        self.output_user_info.should(have.text(f"Name:{simple_user.full_name}"))
        self.output_user_info.should(
            have.text(f"Current Address :{simple_user.current_address}")
        )
        self.output_user_info.should(
            have.text(f"Permananet Address :{simple_user.permanent_address}")
        )

    def register(self, simple_user: SimpleUser):
        self.fill_full_name(simple_user.full_name)
        self.fill_email(simple_user.email)
        self.fill_current_address(simple_user.current_address)
        self.fill_permanent_address(simple_user.permanent_address)
        self.submit()
