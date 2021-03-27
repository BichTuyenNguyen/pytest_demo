import pytest
from hamcrest import assert_that, equal_to
from config.desired_caps import CHROME_LINUX, SAFARI_IPHONE_X
from config.test_users import USERS
from pageobjects.profile_page import ProfilePage
from pageobjects.home_page import HomePage
from pageobjects.login_page import LoginPage


@pytest.mark.parametrize('designed_caps, is_sauce_labs',
                         [(CHROME_LINUX, False), (SAFARI_IPHONE_X, False), (SAFARI_IPHONE_X, True)])
def test_get_user_name(web_driver, designed_caps, is_sauce_labs):
    is_mobile = designed_caps['isMobile']
    driver = web_driver(is_sauce_labs,
                        designed_caps['isMobile'],
                        designed_caps['platformName'],
                        designed_caps['browserName'],
                        designed_caps['deviceName'])
    user = USERS['tuyen']
    # 1. Login
    login_page = LoginPage(driver)
    login_page.navigate_login_page()
    login_page.input_user_email(user['email'])
    login_page.input_user_password(user['password'])
    login_page.click_login_button()
    # 2. Navigate to view profile page
    home_page = HomePage(driver)
    home_page.click_on_menu_list(is_mobile=is_mobile)
    home_page.click_view_profile_option(is_mobile=is_mobile)
    # 3. Get user name
    profile_page = ProfilePage(driver)
    actual_user_name = profile_page.get_user_full_name()
    assert_that(actual_user_name, equal_to('Tuyen Nguyen'), 'Verify the user name')