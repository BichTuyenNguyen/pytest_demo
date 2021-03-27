from pageobjects.locators.login_page_locators import *
from pageobjects.page import BasePage
from config.env_setup import EnvSetup


class LoginPage(BasePage):
    def navigate_login_page(self):
        self.navigate(NAVIGATE_LOGIN.format(site=EnvSetup.SITE))

    def input_user_email(self, email):
        self.set_element_text(USER_EMAIL, email)

    def input_user_password(self, password):
        self.set_element_text(USER_PASSWORD, password)

    def click_login_button(self):
        self.click_element(LOGIN_COMMIT_BUTTON)




