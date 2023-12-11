import random
from faker import Faker

faker_en = Faker('En')


class Data:
    # URL
    URL = 'https://demoqa.com/automation-practice-form'
    # User Data
    gender = ['Male', 'Female', 'Other']

    user = {
        "first_name": faker_en.first_name(),
        "last_name": faker_en.last_name(),
        "gender": random.choice(gender),
        "email": faker_en.email(),
        "mobile": faker_en.msisdn(),
        "subject": "English",
    }
