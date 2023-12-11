import os
import time

from selenium.webdriver import Keys

from generator.generator import generate_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from test_data.data import Data


class FormPage(BasePage):

    def fill_field_and_submit(self):
        path = generate_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(Data.user["first_name"])
        self.element_is_visible(Locators.LAST_NAME).send_keys(Data.user["last_name"])
        self.element_is_visible(Locators.EMAIL).send_keys(Data.user["email"])
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(Data.user["mobile"])
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(Data.user["subject"])
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES)
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(Locators.SUBMIT).click()
        return Data.user

    def form_result(self):
        result_lit = self.element_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_lit]
        return result_text
