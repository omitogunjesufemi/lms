from datetime import time, date


class NewSittingDto:
    participant_id: int
    assessment_id: int
    question_list: list
    answer_list: list
    user_answer: list
    date_submitted: date
    time_submitted: time
    id: int


class RetakeSittingDto:
    participant_id: int
    assessment_id: int
    question_list: list
    answer_list: list
    user_answer: list
    date_submitted: date
    time_submitted: time
    id: int


class ListSittingDto:
    participant_registration_number: str
    participant_id: str
    assessment_id: int
    assessment_course: str
    assessment_title: str
    date_submitted: date
    time_submitted: time
    id: int


class SittingDetailsDto:
    participant_id: int
    participant_first_name: str
    participant_last_name: str
    participant_registration_number: str
    assessment_id: int
    assessment_title: str
    question_list: list
    answer_list: list
    user_answer: list
    date_submitted: date
    time_submitted: time
    id: int
