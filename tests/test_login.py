'''
These tests cover logging in to the Pega Sandbox environment.
'''

from pages.login import PegaLoginPage
from pages.home import PegaHomePage

def test_login(browser):

    login_page = PegaLoginPage(browser)
    home_page = PegaHomePage(browser)
    USERNAME = "author@gogoroad"
    PASSWORD = "pega123!"

    # Given the Pega Sandbox login page is displayed
    login_page.load()

    # When the user enters a valid username and password
    # TODO

    # Then the user will be navigated to the case worker home page
    # TODO

    raise Exception("Incomplete test")

