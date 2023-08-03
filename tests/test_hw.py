import datetime
from demoqa_tests.models.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User

def test_fill_and_submit_form(open_and_close_browser):
    registration_page = RegistrationPage()

    katrin = User(
        first_name='Катрин',
        last_name='Заидова',
        email='newemail@mail.ru',
        gender='Female',
        mobile='9998076767',
        date_of_birth=datetime.date(1995, 8, 24),
        subjects='English',
        hobbies='Reading',
        picture='bear.jpg',
        current_address='Koh Samui, Thailand',
        state="Haryana",
        city="Karnal"
    )

    registration_page.open()
    registration_page.register(katrin)
    registration_page.should_registered_user(katrin)
