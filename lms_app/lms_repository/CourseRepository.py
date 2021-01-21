from abc import abstractmethod, ABCMeta
from typing import List
from lms_app.lms_dto.CourseDto import *
from lms_app.models import Course


class CourseRepository(metaclass=ABCMeta):
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

    def details(self, course_id) -> CourseDetailDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, course_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DjangoORMCourseRepository(CourseRepository):
    def register(self, model: CreateCourseDto):
        course = Course()
        course.course_title = model.course_title
        course.course_description = model.course_description
        course.save()

    def edit(self, course_id, model: EditCourseDto):
        try:
            course = Course.objects.get(id=course_id)
            course.course_title = model.course_title
            course.course_description = model.course_description
            course.save()
        except Course.DoesNotExist as e:
            print('This Course is not yet Registered!')
            raise e

    def list(self) -> List[ListCourseDto]:
        courses = list(Course.objects.values('id',
                                             'course_title',
                                             'course_description',
                                             ))
        course_list: List[ListCourseDto] = []
        for course in courses:
            subject = ListCourseDto()
            subject.id = course['id']
            subject.course_title = course['course_title']
            subject.course_description = course['course_description']
            course_list.append(subject)
        return course_list

    def details(self, course_id) -> CourseDetailDto:
        try:
            course = Course.objects.get(id=course_id)
            subject = CourseDetailDto()
            subject.id = course.id
            subject.course_title = course.course_title
            subject.course_description = course.course_description
            return subject
        except Course.DoesNotExist as e:
            print('This Course is not yet Registered!')
            raise e

    def delete(self, course_id):
        try:
            Course.objects.get(course_id).delete()
        except Course.DoesNotExist as e:
            print('Cannot delete Course because it does not exist!')
            raise e