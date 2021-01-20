class RegisterTutorDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    password: str
    confirm_password: str
    registration_number: str
    id: int


class EditTutorDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    id: int


class ListTutorDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    registration_number: str
    id: int


class TutorDetailsDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    course: int
    appointment: int
    registration_number: str
    id: int