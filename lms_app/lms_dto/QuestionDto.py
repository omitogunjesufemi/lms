class SetQuestionDto:
    question_title: str
    question_content: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    answer: str
    assigned_mark: int
    assessment_id: int
    id: int


class UpdateQuestionDto:
    question_title: str
    question_content: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    answer: str
    assigned_mark: int
    id: int


class ListQuestionDto:
    question_title: str
    assigned_mark: int
    assessment_id: int
    question_content: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    answer: str
    id: int


class GetQuestionDto:
    question_title: str
    question_content: str
    choice1: str
    choice2: str
    choice3: str
    choice4: str
    answer: str
    assigned_mark: int
    assessment_id: int
    id: int