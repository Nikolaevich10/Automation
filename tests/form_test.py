from pages.form_page import FormPage
from test_data.data import Data


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, Data.URL)
        form_page.open()
        form_page.fill_field_and_submit()
        result = form_page.form_result()
        assert f"{Data.user['first_name']} {Data.user['last_name']}" == result[0]
        assert f"{Data.user['email']}" == result[1]
        print(result)

