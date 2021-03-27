import pytest
from selenium import webdriver
from appium import webdriver as appium_webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.env_setup import EnvSetup as EnvConf
from config.desired_caps import SAUCE_LABS_RDC_CHROME_EMULATION_MAPPING


def create_driver(is_mobile, device_name):
    chrome_options = ChromeOptions()
    if is_mobile:
        # Device name should be "Pixel 2", "Nexus 5", "iPhoneX", "iPad Mini" ...
        device_name_emulation = SAUCE_LABS_RDC_CHROME_EMULATION_MAPPING[device_name]
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": device_name_emulation})
    if EnvConf.HEADLESS:
        chrome_options.add_argument("--headless")
    if EnvConf.NO_SANDBOX:
        chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    return browser


@pytest.fixture()
def web_driver(request):
    driver_lst = []
    rdc_user = EnvConf.SAUCE_LABS_RDC_USER
    rdc_key = EnvConf.SAUCE_LABS_RDC_KEY

    def _web_driver(is_sauce_labs=False,
                    is_mobile=False,
                    platform=EnvConf.PLATFORM,
                    browser_name=EnvConf.BROWSER_NAME,
                    device_name=None):
        test_name = request.node.name
        if is_sauce_labs:
            caps = {'browserName': browser_name, 'platformName': platform, 'deviceName': device_name,
                    'name': test_name, 'build': EnvConf.BUILD_TAG
                    }
            grid_url = \
                "https://{}:{}@ondemand.us-west-1.saucelabs.com:443/wd/hub".format(rdc_user, rdc_key)
            browser = appium_webdriver.Remote(grid_url, desired_capabilities=caps)
        else:
            browser = create_driver(is_mobile, device_name)
            browser.maximize_window()

        if browser is not None:
            print("SauceOnDemandSessionID={} job-name={}".format(browser.session_id, test_name))
        else:
            raise WebDriverException("Never created!")

        browser.set_page_load_timeout(EnvConf.PAGE_LOAD_TIMEOUT_SECONDS)
        driver_lst.append(browser)
        return browser

    yield _web_driver
    if getattr(driver_lst[0], "battery_info", None):
        sauce_result = "failed" if request.node.rep_call.failed else "passed"
        driver_lst[0].execute_script("sauce:job-result={}".format(sauce_result))
    driver_lst[0].quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for Sauce Labs reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)