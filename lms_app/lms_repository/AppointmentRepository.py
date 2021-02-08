from abc import ABCMeta, abstractmethod
from typing import List

from lms_app.lms_dto.AppointmentDto import *
from lms_app.models import Appointment


class AppointmentRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, model: InitiatedAppointmentDto):
        """Appoint a tutor for a Course"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, appointment_id, model: UpdatedAppointmentDto):
        """Update a Tutor Appointed Courses"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListAppointmentDto]:
        """List the teachers and courses appointed"""
        raise NotImplementedError

    @abstractmethod
    def list_appoint_for_tutor(self, tutor_id) -> List[ListAppointmentDto]:
        """List the teachers and courses appointed"""
        raise NotImplementedError

    @abstractmethod
    def list_tutor_for_course_appointed(self, course_id) -> List[ListAppointmentDto]:
        """List the teachers and courses appointed"""
        raise NotImplementedError

    @abstractmethod
    def details(self, tutors_id) -> AppointmentDetailsDto:
        """Details of a particular appointment"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, appointment_id):
        """Delete an appointment for a course"""
        raise NotImplementedError


class DjangoORMAppointmentRepository(AppointmentRepository):
    def register(self, model: InitiatedAppointmentDto):
        appointment = Appointment()
        appointment.course_id = model.course_id
        appointment.tutors_id = model.tutors_id
        appointment.date_appointed = model.date_appointed

        appointment.save()
        appointment.tutors.save()
        appointment.course.save()

    def edit(self, appointment_id, model: UpdatedAppointmentDto):
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.course.id = model.course_id
            appointment.tutors.id = model.tutors_id

            appointment.save()
            appointment.tutors.save()
            appointment.course.save()
        except Appointment.DoesNotExist as e:
            print('No appointment found!')
            raise e

    def list(self) -> List[ListAppointmentDto]:
        appointments = list(Appointment.objects.values('id', 'tutors__user__first_name', 'tutors__user__last_name',
                                                       'course__course_title',
                                                       'tutors__registration_number',
                                                       'tutors_id',
                                                       'course_id'))

        appointment_list: List[ListAppointmentDto] = []
        for appointment in appointments:
            contract = ListAppointmentDto()
            contract.id = appointment['id']
            contract.course_title = appointment['course__course_title']
            contract.course_id = appointment['course_id']
            contract.tutors_first_name = appointment['tutors__user__first_name']
            contract.tutors_last_name = appointment['tutors__user__last_name']
            contract.tutors_reg = appointment['tutors__registration_number']
            contract.tutors_id = appointment['tutors_id']
            appointment_list.append(contract)
        return appointment_list

    def list_appoint_for_tutor(self, tutor_id) -> List[ListAppointmentDto]:
        appointments = list(Appointment.objects.values('id', 'tutors__user__first_name', 'tutors__user__last_name',
                                                       'course__course_title',
                                                       'course__course_slug',
                                                       'tutors__registration_number',
                                                       'tutors_id',
                                                       'course_id'))

        appointment_list: List[ListAppointmentDto] = []
        for appointment in appointments:
            if tutor_id == appointment['tutors_id']:
                contract = ListAppointmentDto()
                contract.id = appointment['id']
                contract.course_title = appointment['course__course_title']
                contract.course_description = appointment['course__course_slug']
                contract.course_id = appointment['course_id']
                contract.tutors_first_name = appointment['tutors__user__first_name']
                contract.tutors_last_name = appointment['tutors__user__last_name']
                contract.tutors_reg = appointment['tutors__registration_number']
                contract.tutors_id = appointment['tutors_id']
                appointment_list.append(contract)
        return appointment_list

    def list_tutor_for_course_appointed(self, course_id) -> List[ListAppointmentDto]:
        appointments = list(Appointment.objects.values('id', 'tutors__user__first_name', 'tutors__user__last_name',
                                                       'course__course_title',
                                                       'tutors__registration_number',
                                                       'tutors_id',
                                                       'course_id'))

        appointment_list: List[ListAppointmentDto] = []
        for appointment in appointments:
            if course_id == appointment['course_id']:
                contract = ListAppointmentDto()
                contract.id = appointment['id']
                contract.course_title = appointment['course__course_title']
                contract.course_id = appointment['course_id']
                contract.tutors_first_name = appointment['tutors__user__first_name']
                contract.tutors_last_name = appointment['tutors__user__last_name']
                contract.tutors_reg = appointment['tutors__registration_number']
                contract.tutors_id = appointment['tutors_id']
                appointment_list.append(contract)
        return appointment_list

    def details(self, tutors_id) -> AppointmentDetailsDto:
        try:
            appointment = Appointment.objects.get(tutors_id=tutors_id)
            contract = AppointmentDetailsDto()
            contract.id = appointment.id
            contract.course_id = appointment.course.id
            contract.tutors_id = appointment.tutors.id
            contract.tutors_first_name = appointment.tutors.first_name
            contract.tutors_last_name = appointment.tutors.last_name
            contract.tutors_registration_number = appointment.tutors.registration_number
            contract.date_appointed = appointment.date_appointed
            return contract
        except Appointment.DoesNotExist as e:
            print('No appointment found!')
            raise e

    def delete(self, appointment_id):
        try:
            Appointment.objects.get(appointment_id).delete()
        except Appointment.DoesNotExist as e:
            print('Cannot delete as you are not appointed for the course!')
            raise e
