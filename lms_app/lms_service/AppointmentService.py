from lms_app.lms_repository import AppointmentRepository
from lms_app.lms_repository.AppointmentRepository import *


class AppointmentManagementService(metaclass=ABCMeta):
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
    def details(self, tutors_id) -> AppointmentDetailsDto:
        """Details of a particular appointment"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, appointment_id):
        """Delete an appointment for a course"""
        raise NotImplementedError


class DefaultAppointmentManagementService(AppointmentManagementService):
    repository = AppointmentRepository

    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def register(self, model: InitiatedAppointmentDto):
        return self.repository.register(model)

    def edit(self, appointment_id, model: UpdatedAppointmentDto):
        return self.repository.edit(model)

    def list(self) -> List[ListAppointmentDto]:
        return self.repository.list()

    def list_appoint_for_tutor(self, tutor_id) -> List[ListAppointmentDto]:
        return self.repository.list_appoint_for_tutor(tutor_id)

    def details(self, tutors_id) -> AppointmentDetailsDto:
        return self.repository.details(tutors_id)

    def delete(self, appointment_id):
        return self.repository.delete(appointment_id)