from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def complete_information(self, first_name, last_name, postal_code):
        first_name_input = self.find_visible(self.FIRST_NAME_INPUT)
        last_name_input = self.find_visible(self.LAST_NAME_INPUT)
        postal_code_input = self.find_visible(self.POSTAL_CODE_INPUT)

        self.driver.execute_script(
            """
            const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                window.HTMLInputElement.prototype,
                'value'
            ).set;
            const values = [arguments[3], arguments[4], arguments[5]];
            [arguments[0], arguments[1], arguments[2]].forEach((input, index) => {
                nativeInputValueSetter.call(input, values[index]);
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
            });
            """,
            first_name_input,
            last_name_input,
            postal_code_input,
            first_name,
            last_name,
            postal_code,
        )
        self.click(self.CONTINUE_BUTTON)

    def finish_purchase(self):
        self.click(self.FINISH_BUTTON)

    def confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)
