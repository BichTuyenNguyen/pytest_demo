from pageobjects.page import BasePage


class ImagePage(BasePage):

    def get_camera_model(self, locator):
        return self.get_element_text(locator)

    def get_focal_length(self, locator):
        return self.get_element_text(locator)

    def get_related_tags(self, locator):
        return self.get_element_texts(locator)

    def download_image(self, locator):
        attribute = "src"
        return self.get_attribute_of_element(locator, attribute)

    def download_image_using_href(self, locator):
        attribute = "href"
        return self.get_attribute_of_element(locator, attribute)


