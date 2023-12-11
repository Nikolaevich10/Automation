from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    mobile: str = None
    current_address: str = None
    permanent_address: str = None
