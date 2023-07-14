from selene import browser
from selene import be, have, command

from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.element('#adplus-anchor').perform(command.js.remove)
        browser.element('#close-fixedban').perform(command.js.remove)
        browser.element('footer').perform(command.js.remove)

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_user_email(self, value):
        browser.element('#userEmail').type(value)

    def gender_click(self):
        browser.element('[for="gender-radio-2"]').click()

    def type_user_number(self, value):
        browser.element('.col-md-9 [id="userNumber"]').type(value)

    def type_date_of_birth_input(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').should(be.clickable).click()

    def subjects_input(self, value):
        browser.element('#subjectsInput').click()
        browser.element('#subjectsInput').type(value).press_enter()

    def hobbi_checkbox_click(self):
        browser.element('[for="hobbies-checkbox-2"]').click()

    def upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(resource.path(file_name))

    def type_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def state_and_city_click(self, state, city):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def submit_click(self):
        browser.element('#submit').click()

    def should_have_modal_with(self, text):
        browser.element('.modal-header').should(have.exact_text(text))

    def register_user_data(self):
        return browser.element('.table').all('td').even


