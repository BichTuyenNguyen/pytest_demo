from pageobjects.locators.home_page_locators import *
from pageobjects.page import BasePage
from config.env_setup import EnvSetup


class HomePage(BasePage):
    def click_on_menu_list(self, is_mobile):
        if is_mobile:
            self.click_element(MENU_LIST_MOB)
        else:
            self.click_element(MENU_LIST)

    def click_view_profile_option(self, is_mobile):
        if is_mobile:
            self.click_element(VIEW_PROFILE_OPTION_MOB)
        else:
            self.click_element(VIEW_PROFILE_OPTION)




