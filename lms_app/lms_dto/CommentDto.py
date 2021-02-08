from datetime import datetime


class CommentDto:
    username: str
    body: str
    date_created: datetime
    assessment_id: int
