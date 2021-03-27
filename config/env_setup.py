import os

from helper.data_helper import DataHelper


class EnvSetup:
    SITE = os.getenv('SITE', 'https://unsplash.com')
    API = os.getenv('API', 'https://unsplash.com/napi')
    TOKEN = os.getenv('TOKEN', '42ef72d98b48573570f34df9496bdfc643607580f0246152413601e1bd2d5a04')
    PAGE_LOAD_TIMEOUT_SECONDS = 60
    SELENIUM_TIMEOUT_SECONDS = 60

    HEADLESS = DataHelper.str_to_bool(os.getenv('HEADLESS', 'False'))
    NO_SANDBOX = DataHelper.str_to_bool(os.getenv('NO_SANDBOX', 'True'))
    BROWSER_NAME = os.getenv('BROWSER', 'Chrome')
    PLATFORM = os.getenv('PLATFORM', 'WINDOWS')

    SAUCE_LABS = DataHelper.str_to_bool(os.getenv('SAUCE_LABS', 'True'))
    BUILD_TAG = os.getenv('BUILD_TAG', 'Default Sauce Labs Build')
    SAUCE_LABS_RDC_USER = 'zenfolio'
    SAUCE_LABS_RDC_KEY = '26fcdbb3-0a93-4f51-bc44-8f00e81f46bf'
