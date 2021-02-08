class CreateCourseDto:
    course_title: str
    course_slug: str
    file: zip
    id: int


class EditCourseDto:
    course_title: str
    course_slug: str
    course_description: str
    file: zip
    id: int


class ListCourseDto:
    course_title: str
    course_slug: str
    file: zip
    id: int

# class SelectCourseDto:
#     id: int
#     course_title: str


class CourseDetailDto:
    course_title: str
    course_slug: str
    course_description: str
    file: zip
    id: int