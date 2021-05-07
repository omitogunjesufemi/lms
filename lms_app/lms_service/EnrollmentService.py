from abc import abstractmethod, ABCMeta

from lms_app.lms_repository.EnrollmentRepository import *


class EnrollmentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: InitiateEnrollmentDto):
        """Enroll a student for a Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, enrollment_id, model: UpdateEnrollmentDto):
        """Update a Student Registered Courses"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListEnrollmentDto]:
        """List the student and courses enrolled"""
        raise NotImplementedError

    def list_enrollment_for_student(self, student_id) -> List[ListEnrollmentDto]:
        """List the student and courses enrolled"""
        raise NotImplementedError

    def list_student_for_enrollment(self, course_id) -> List[ListEnrollmentDto]:
        """List the student and courses enrolled"""
        raise NotImplementedError

    def list_enrollments_assigned_to_tutor(self, tutor_id) -> List[ListEnrollmentDto]:
        """List the student assigned to a particular tutor"""
        raise NotImplementedError

    def details(self, enrollment_id) -> EnrollmentDetailsDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, enrollment_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DefaultEnrollmentManagementService(EnrollmentManagementService):
    repository = EnrollmentRepository

    def __init__(self, repository: EnrollmentRepository):
        self.repository = repository

    def register(self, model: InitiateEnrollmentDto):
        return self.repository.register(model)

    def edit(self, enrollment_id, model: UpdateEnrollmentDto):
        return self.repository.edit(model)

    def list(self) -> List[ListEnrollmentDto]:
        return self.repository.list()

    def list_student_for_enrollment(self, course_id) -> List[ListEnrollmentDto]:
        return self.repository.list_student_for_enrollment(course_id)

    def list_enrollment_for_student(self, student_id) -> List[ListEnrollmentDto]:
        return self.repository.list_enrollment_for_student(student_id)

    def list_enrollments_assigned_to_tutor(self, tutor_id) -> List[ListEnrollmentDto]:
        return self.repository.list_enrollments_assigned_to_tutor(tutor_id)

    def details(self, enrollment_id) -> EnrollmentDetailsDto:
        return self.repository.details(enrollment_id)

    def delete(self, enrollment_id):
        return self.repository.delete(enrollment_id)