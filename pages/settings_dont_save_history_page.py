from base_classes.driver import Driver


class DontSaveHistoryPage(Driver):

    def get_color_svg_element(self, svg_element):
        return self.driver.execute_script("return arguments[0].getAttribute('fill');", svg_element)

