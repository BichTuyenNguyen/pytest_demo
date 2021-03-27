from selenium.webdriver.common.by import By

LOGIN_PAGE = {
    "NAVIGATE_LOGIN": '{site}/login',
    "USER_EMAIL": (By.ID, 'user_email'),
    "USER_PASSWORD": (By.ID, 'user_password'),
    "LOGIN_COMMIT_BUTTON": (By.NAME, 'commit'),
}

COLLECTION_PAGE = {
    "NAVIGATE_COLLECTIO_PAGE": '{site}/@{username}/collections',
    "NAVIGATE_COLLECTION_PANGE": '{site}/@{username}/collections',
    "EXIST_PHOTOS": (By.XPATH, '//figure[1]'),
    "PHOTO_URL": '{site}/collections/{collection_id}',
}

EDIT_PROFILE_PAGE = {
    "NAVIGATE_EDIT_PROFILE_PAGE": '{site}/account',
    "USER_NAME": (By.XPATH, '//div[@data-test="users-route"]//div[string-length(text())>0][1]'),
    "USER_LOCATION": (By.ID, 'user_location'),
    "UPDATE_PROFILE_BUTTON": (By.XPATH, '//input[@name="commit" and @value="Update account"]')
}

IMAGE_PAGE = {
    "NAVIGATE_INFO_IMAGE_PAGE": '{site}/photos/{photo_id}/info',
    "CAMERA_MODEL": (By.XPATH, '//dt[text()="Camera Model"]/following-sibling::dd'),
    "FOCAL_LENGTH": (By.XPATH, '//dt[text()="Focal Length"]/following-sibling::dd'),
    "RELATED_TAGS": (By.XPATH, '//p[text()="Related tags"]//following-sibling::div//a'),
    "DOWNLOADABLE_IMAGE": (By.XPATH, '//div[@data-test="photos-route"]//button/div[2]/img'),
    "DOWNLOADABLE_BUTTON": (By.XPATH, '//div[@data-test="photos-route"]//div[3]/a[1]'),
}
