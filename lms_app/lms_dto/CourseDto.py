class CreateCourseDto:
    course_title: str
    course_description: str
    id: int


class EditCourseDto:
    course_title: str
    course_description: str
    id: int


class ListCourseDto:
    course_title: str
    course_description: str
    id: int

# class SelectCourseDto:
#     id: int
#     course_title: str


class CourseDetailDto:
    course_title: str
    course_description: str
    id: int