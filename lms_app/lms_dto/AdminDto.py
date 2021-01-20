class RegisterAdminDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    password: str
    confirm_password: str
    id: int


class EditAdminDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    id: int


class ListAdminDto:
    first_name: str
    last_name: str
    email: str
    username: str
    id: int


class AdminDetailsDto:
    first_name: str
    last_name: str
    email: str
    phone: str
    username: str
    course: int
    enrollment: int
    id: int