from selene import browser, have


class Panel:
    def __init__(self):
        self.container = browser.element(".left-pannel")

    def open(self, item):
        browser.open("/elements")
        self.container.all(".menu-list .btn").element_by(have.text(item)).click()

    def open_simple_registration(self):
        self.open("Text Box")
