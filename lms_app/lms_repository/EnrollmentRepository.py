from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.EnrollmentDto import *
from lms_app.models import Enrollment, Sitting, Grading


class EnrollmentRepository(metaclass=ABCMeta):
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

    def details(self, enrollment_id) -> EnrollmentDetailsDto:
        """Details of a particular enrollment"""
        raise NotImplementedError

    def delete(self, enrollment_id):
        """Delete an enrollment for a course"""
        raise NotImplementedError


class DjangoORMEnrollmentRepository(EnrollmentRepository):
    def register(self, model: InitiateEnrollmentDto):
        enrollment = Enrollment()
        enrollment.course_id = model.course_id
        enrollment.student_id = model.student_id
        enrollment.date_enrolled = model.date_enrolled

        enrollment.save()
        enrollment.course.save()
        enrollment.student.save()

    def edit(self, enrollment_id, model: UpdateEnrollmentDto):
        try:
            enrollment = Enrollment.objects.get(id=enrollment_id)
            enrollment.course.id = model.course_id
            enrollment.save()
            enrollment.course.save()
        except Enrollment.DoesNotExist as e:
            print('This Student is not enrolled for this course!')
            raise e

    def list(self) -> List[ListEnrollmentDto]:
        enrollments = list(Enrollment.objects.values('id', 'student_id',
                                                     'student__registration_number',
                                                     'course__course_title',
                                                     'course_id',
                                                     'date_enrolled'
                                                     ))

        appointment_list: List[ListEnrollmentDto] = []
        for enrollment in enrollments:
            contract = ListEnrollmentDto()
            contract.id = enrollment['id']
            contract.course_id = enrollment['course_id']
            contract.course_title = enrollment['course__course_title']
            contract.student_id = enrollment['student_id']
            contract.student_registration_number = enrollment['student__registration_number']
            contract.date_enrolled = enrollment['date_enrolled']
            appointment_list.append(contract)
        return appointment_list

    def list_enrollment_for_student(self, student_id) -> List[ListEnrollmentDto]:
        enrollments = list(Enrollment.objects.values('id', 'student_id',
                                                     'student__registration_number',
                                                     'course__course_title',
                                                     'course__course_description',
                                                     'course_id',
                                                     'date_enrolled'
                                                     ))

        appointment_list: List[ListEnrollmentDto] = []
        for enrollment in enrollments:
            if student_id == enrollment['student_id']:
                contract = ListEnrollmentDto()
                contract.id = enrollment['id']
                contract.course_id = enrollment['course_id']
                contract.course_title = enrollment['course__course_title']
                contract.course_description = enrollment['course__course_description']
                contract.student_id = enrollment['student_id']
                contract.student_registration_number = enrollment['student__registration_number']
                contract.date_enrolled = enrollment['date_enrolled']
                appointment_list.append(contract)
        return appointment_list

    def details(self, enrollment_id) -> EnrollmentDetailsDto:
        try:
            enrollment = Enrollment.objects.get(id=enrollment_id)
            contract = EnrollmentDetailsDto()
            contract.id = enrollment_id
            contract.course_id = enrollment.course.id
            contract.course_title = enrollment.course.course_title
            contract.student_id = enrollment.student.id
            contract.student_first_name = enrollment.student.user.first_name
            contract.student_last_name = enrollment.student.user.last_name
            contract.student_email = enrollment.student.user.email
            contract.student_registration_number = enrollment.student.registration_number
            contract.date_enrolled = enrollment.date_enrolled
            return contract
        except Enrollment.DoesNotExist as e:
            print('No enrollment found!')
            raise e

    def delete(self, enrollment_id):
        try:
            enrollment = Enrollment.objects.get(id=enrollment_id)
            student_id = enrollment.student_id
            sittings = Sitting.objects.all()
            sitting = []
            for sitting__ in sittings:
                if student_id == sitting__.participant_id:
                    sitting.append(sitting__)

            if len(sitting) == 0:
                pass
            elif len(sitting) == 1:
                sitting_id = sitting[0].id
                grading = Grading.objects.get(sitting_id=sitting_id)
                grading.delete()
                Sitting.objects.get(id=sitting_id).delete()
            elif len(sitting) > 1:
                for sit in sitting:
                    sitting_id = sitting[sit].id
                    grading = Grading.objects.get(sitting_id=sitting_id)
                    grading.delete()
                    Sitting.objects.get(id=sitting_id).delete()

            enrollment.delete()
        except Enrollment.DoesNotExist as e:
            print('Cannot delete as you are not enrolled for the course!')
            raise e
