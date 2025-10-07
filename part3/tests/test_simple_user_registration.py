from part3.Application import app
from part3.data import users


def test_registers_simple_user(setup_browser):
    app.panel.open_simple_registration()

    app.simple_registration.register(users.simple_user)

    app.simple_registration.should_have_submited(users.simple_user)
