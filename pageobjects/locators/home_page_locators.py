from selenium.webdriver.common.by import By


MENU_LIST = (By.ID, 'popover-avatar-loggedin-menu-desktop')
MENU_LIST_MOB = (By.ID, 'popover-avatar-loggedin-menu-mobile')
VIEW_PROFILE_OPTION = (By.XPATH, '//div[@id="popover-avatar-loggedin-menu-desktop"]//a[text()="View profile"]')
VIEW_PROFILE_OPTION_MOB = (By.XPATH, '//div[@id="popover-avatar-loggedin-menu-mobile"]//a[text()="View profile"]')
