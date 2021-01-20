from datetime import date


class InitiateEnrollmentDto:
    id: int
    student_id: int
    course_id: int
    date_enrolled: date


class UpdateEnrollmentDto:
    course_id: int
    id: int


class ListEnrollmentDto:
    student_id: int
    student_registration_number: str
    course_title: str
    course_description: str
    course_id: int
    date_enrolled: date
    id: int


class EnrollmentDetailsDto:
    student_id: int
    course_id: int
    student_first_name: str
    student_last_name: str
    student_registration_number: str
    student_email: str
    course_title: str
    date_enrolled: date
    id: int