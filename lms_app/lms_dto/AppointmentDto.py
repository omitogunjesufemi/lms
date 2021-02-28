from datetime import date


class InitiatedAppointmentDto:
    tutors_id: int
    course_id: int
    date_appointed: date
    id: int


class UpdatedAppointmentDto:
    tutors_id: int
    course_id: int
    id: int


class ListAppointmentDto:
    tutors_first_name: str
    tutors_reg: str
    tutors_last_name: str
    course_title: str
    course_description: str
    date_appointed: date
    course_id: int
    tutors_id: int
    id: int


class AppointmentDetailsDto:
    tutors_id: int
    tutors_first_name: int
    tutors_last_name: int
    tutors_registration_number: str
    course_title: int
    course_id: int
    date_appointed: date
    id: int
