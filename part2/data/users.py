import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    number: str
    gender: str
    birth_date: dict
    subjects: list
    hobbies: list
    address: str
    state: str
    city: str
    image_name: str


student = User(
    first_name="Kirill",
    last_name="Semin",
    email="testemail1324@gmail.com",
    number="9803628839",
    gender="Male",
    birth_date={"day": 20, "month": "January", "year": 1999},
    subjects=["Maths", "English", "Physics", "Chemistry", "Computer Science"],
    hobbies=["Sports", "Reading"],
    address="Emlutina 13",
    state="NCR",
    city="Delhi",
    image_name="cat.jpg",
)
