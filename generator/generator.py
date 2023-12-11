import os
import random

from test_data.user_data import Person
from faker import Faker

faker = Faker('En')


def generated_person():
    return Person(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        mobile=faker.msisdn(),
        current_address=faker.address(),
        permanent_address=None,
        subject='English'
    )


def generate_file():
    path = os.path.join("/Users/aleksandr/PycharmProjects/QaAutomation", f"{random.randint(1, 5)}.txt")
    file = open(path, 'w')
    file.write(f'{random.randint(1, 100)}')
    file.close()
    return path
