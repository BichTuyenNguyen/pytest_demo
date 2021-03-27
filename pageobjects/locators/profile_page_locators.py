from selenium.webdriver.common.by import By

USER_NAME = (By.XPATH, '//div[@data-test="users-route"]//div[string-length(text())>0][1]')
USER_LOCATION = (By.ID, 'user_location')
UPDATE_PROFILE_BUTTON = (By.XPATH, '//input[@name="commit" and @value="Update account"]')
