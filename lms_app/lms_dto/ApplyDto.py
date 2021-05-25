class ApplyDto:
    tutor_id: int
    status: bool
    course_id: int
    qualifications: str
    file: zip

class ListApplyDto:
    tutor_id: int
    tutor_registration_number: str
    course_title: str
    status: bool
    course_id: int
    qualifications: str