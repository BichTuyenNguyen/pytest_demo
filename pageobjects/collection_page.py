from pageobjects.page import BasePage


class CollectionPage(BasePage):
    def select_photo(self, locator):
        return self.click_element(locator)
