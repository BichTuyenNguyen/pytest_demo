from pageobjects.locators.profile_page_locators import USER_NAME
from pageobjects.page import BasePage


class ProfilePage(BasePage):
    def get_user_full_name(self, ):
        return self.get_element_text(USER_NAME)
