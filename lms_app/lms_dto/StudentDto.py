class RegisterStudentDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    password: str
    confirm_password: str
    registration_number: str
    id: int


class EditStudentDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    id: int


class ListStudentDto:
    first_name: str
    last_name: str
    email: str
    username: str
    registration_number: str
    id: int


class StudentDetailsDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    course: int
    enrollment: int
    registration_number: str
    id: int