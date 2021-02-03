from abc import abstractmethod, ABCMeta

from lms_app.lms_repository import CourseRepository
from lms_app.lms_repository.CourseRepository import *


class CourseManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: CreateCourseDto):
        """Enroll a student for a Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, course_id, model: EditCourseDto):
        """Update a Student Registered Courses"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListCourseDto]:
        """List the student and courses enrolled"""
        raise NotImplementedError

    @abstractmethod
    def details(self, course_id) -> CourseDetailDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, course_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DefaultCourseManagementService(CourseManagementService):
    repository = CourseRepository

    def __init__(self, repository: CourseRepository):
        self.repository = repository

    def register(self, model: CreateCourseDto):
        return self.repository.register(model)

    def edit(self, course_id, model: EditCourseDto):
        return self.repository.edit(course_id, model)

    def list(self) -> List[ListCourseDto]:
        return self.repository.list()

    def details(self, course_id) -> CourseDetailDto:
        return self.repository.details(course_id)

    def delete(self, course_id):
        return self.repository.delete(course_id)