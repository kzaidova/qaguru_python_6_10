from selene import have

from demoqa_tests.models.pages.registration_page import RegistrationPage


def test_fill_and_submit_form(open_and_close_browser):
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.type_first_name('Катрин')
    registration_page.type_last_name('Заидова')
    registration_page.type_user_email('newemail@mail.ru')
    registration_page.gender_click()
    registration_page.type_user_number('9998076767')
    registration_page.type_date_of_birth_input('1995', 'August', 24)
    registration_page.subjects_input('Eng')
    registration_page.hobbi_checkbox_click()
    registration_page.upload_picture('bear.jpg')
    registration_page.type_current_address('Koh Samui, Thailand')
    registration_page.state_and_city_click("Haryana", "Karnal")
    registration_page.submit_click()

    registration_page.should_have_modal_with('Thanks for submitting the form')
    registration_page.register_user_data().should(
            have.exact_texts(
        'Катрин Заидова',
        'newemail@mail.ru',
        'Female',
        '9998076767',
        '24 August,1995',
        'English',
        'Reading',
        'bear.jpg',
        'Koh Samui, Thailand',
        'Haryana Karnal'
            )
    )

