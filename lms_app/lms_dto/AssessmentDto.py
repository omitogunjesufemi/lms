from datetime import date, time


class CreateAssessmentDto:
    assessment_title: str
    assessment_content: str
    total_score: int
    pass_mark: int
    course_id: int
    date_due: date
    time_due: time
    id: int


class UpdateAssessmentDto:
    assessment_title: str
    assessment_content: str
    total_score: int
    pass_mark: int
    course_id: int
    questions_id: int
    date_due: date
    time_due: time
    status: int
    id: int


class ListAssessmentDto:
    assessment_title: str
    total_score: int
    pass_mark: int
    course_id: int
    course_title: str
    date_due: date
    time_due: time
    status: bool
    id: int


class AssessmentDetailsDto:
    assessment_title: str
    assessment_content: str
    course_id: int
    total_score: int
    pass_mark: int
    course_title: str
    questions_id: int
    date_due: date
    time_due: time
    status: bool
    id: int